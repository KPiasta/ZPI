using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication3
{
    public class CrawlerManager
    {
        public static string dest = AppDomain.CurrentDomain.BaseDirectory + "..\\..\\files_stuff\\result\\result.txt";
        public enum CrawlerMode
        {
            single = 0,
            list = 1,
            category = 2
        }

        public static void runCrawlers(String querry, CrawlerMode mode = CrawlerMode.single)
        {
            string dir = AppDomain.CurrentDomain.BaseDirectory;
            string strCmdText;
            strCmdText = string.Format("/C python.exe  {0}..\\..\\main.py \"{1}\" {0}..\\..\\files_stuff\\result\\result.txt {2}", dir, querry, (int)mode);
            var proc = System.Diagnostics.Process.Start("CMD.exe", strCmdText);
            proc.WaitForExit();
        }
    }
}