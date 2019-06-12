using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication3
{
    public class CrawlerManager
    {
        public static string dest = AppDomain.CurrentDomain.BaseDirectory + "..\\..\\files_stuff\\result\\result.txt";
        public static string imgs = AppDomain.CurrentDomain.BaseDirectory + "..\\..\\files_stuff\\result\\images.txt";
        public static string main = AppDomain.CurrentDomain.BaseDirectory + "..\\..\\main.py";
        public enum CrawlerMode
        {
            single = 0,
            list = 1,
            category = 2,
            images=3
        }

        public static void RunCrawlers(String querry, CrawlerMode mode = CrawlerMode.single,int low=0,int high=0)
        {
            
            string strCmdText;
            if (mode == CrawlerMode.images)
            {
                strCmdText = string.Format("/C python.exe  {0} \"{1}\" {2} {3} {4} {5}", main, querry,imgs, (int)mode, low, high);
            }
            else
            {
                strCmdText = string.Format("/C python.exe  {0} \"{1}\" {2} {3}",main, querry,dest, (int)mode);
            }
            var proc = System.Diagnostics.Process.Start("CMD.exe", strCmdText);
            proc.WaitForExit();
        }
    }
}