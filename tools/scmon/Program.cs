// Read-only SimConnect monitor: prints a timestamped line whenever a watched SimVar changes.
// It never writes to the sim. Optionally it also polls one B-Var through the PilotsDeck API.
//
// Usage: dotnet <out>\scmon.dll [seconds] [B-var]
//   seconds  how long to watch (default 180)
//   B-var    an input event to poll through PilotsDeck's local API, e.g. B:electrical_battery_1
//            (the API can read B-Vars and L-Vars, but not A-Vars whose names contain spaces)
//
// Edit the Vars list below to watch other SimVars.
using System.Net.Http;
using Microsoft.FlightSimulator.SimConnect;

enum DEF { D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15 }

static class Program
{
    static readonly (string Name, string Unit, string Label)[] Vars =
    {
        ("ELECTRICAL MASTER BATTERY:1", "Bool", "BAT:1"),
        ("ELECTRICAL MASTER BATTERY:2", "Bool", "BAT:2"),
        ("GENERAL ENG MASTER ALTERNATOR:1", "Bool", "ALT:1"),
        ("BRAKE PARKING POSITION", "Bool", "PARK"),
        ("AUTOPILOT MASTER", "Bool", "AP"),
        ("PLANE HEADING DEGREES MAGNETIC", "Degrees", "HDG"),
    };
    static readonly double[] Values = Enumerable.Repeat(double.NaN, Vars.Length).ToArray();
    static string BvarName;
    static string Bvar = "?";
    static string Last = "";

    static void Print()
    {
        var parts = Vars.Select((v, i) =>
            $"{v.Label}={(double.IsNaN(Values[i]) ? "?" : Math.Abs(Values[i] % 1) > 0.0001 ? Values[i].ToString("0.0") : Values[i].ToString("0"))}");
        string line = string.Join("  ", parts) + (BvarName != null ? $"  | plugin {BvarName}={Bvar}" : "");
        if (line != Last) { Console.WriteLine($"{DateTime.Now:HH:mm:ss.f}  {line}"); Last = line; }
    }

    static int Main(string[] args)
    {
        int seconds = args.Length > 0 ? int.Parse(args[0]) : 180;
        BvarName = args.Length > 1 ? args[1] : null;
        if (Vars.Length > Enum.GetValues<DEF>().Length) { Console.WriteLine("Too many Vars: add entries to DEF."); return 2; }

        var wait = new AutoResetEvent(false);
        SimConnect sc;
        try { sc = new SimConnect("scmon (read-only)", IntPtr.Zero, 0, wait, 0); }
        catch (Exception ex) { Console.WriteLine($"Could not connect to MSFS: {ex.Message}"); return 1; }

        sc.OnRecvException += (s, e) => Console.WriteLine($"SimConnect exception {(SIMCONNECT_EXCEPTION)e.dwException} (send {e.dwSendID}, index {e.dwIndex})");
        sc.OnRecvSimobjectData += (s, e) => { Values[(int)e.dwRequestID] = (double)e.dwData[0]; Print(); };

        for (int i = 0; i < Vars.Length; i++)
        {
            var def = (DEF)i;
            sc.AddToDataDefinition(def, Vars[i].Name, Vars[i].Unit, SIMCONNECT_DATATYPE.FLOAT64, 0, SimConnect.SIMCONNECT_UNUSED);
            sc.RegisterDataDefineStruct<double>(def);
            sc.RequestDataOnSimObject(def, def, SimConnect.SIMCONNECT_OBJECT_ID_USER, SIMCONNECT_PERIOD.SIM_FRAME, SIMCONNECT_DATA_REQUEST_FLAG.CHANGED, 0, 0, 0);
        }

        using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(2) };
        const string api = "http://localhost:42042/v1";
        if (BvarName != null) { try { http.GetAsync($"{api}/register/{BvarName}").Wait(); } catch { } }

        Console.WriteLine($"Watching for {seconds}s ...");
        var end = DateTime.Now.AddSeconds(seconds);
        var nextPoll = DateTime.MinValue;
        while (DateTime.Now < end)
        {
            if (wait.WaitOne(100)) sc.ReceiveMessage();
            if (BvarName != null && DateTime.Now >= nextPoll)
            {
                try { Bvar = http.GetStringAsync($"{api}/get/{BvarName}").Result.Trim(); } catch { Bvar = "ERR"; }
                Print();
                nextPoll = DateTime.Now.AddMilliseconds(500);
            }
        }

        if (BvarName != null) { try { http.GetAsync($"{api}/unregister/{BvarName}").Wait(); } catch { } }
        sc.Dispose();
        Console.WriteLine("done");
        return 0;
    }
}
