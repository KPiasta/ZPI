using System;
using System.Diagnostics;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class SiteMaster : MasterPage
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            runCrawlers(TextBox1.Text);
            Response.Redirect("SearchResults.aspx");
        }
        protected void runCrawlers(String querry)
        {
            string dir =AppDomain.CurrentDomain.BaseDirectory;
            string strCmdText;
            strCmdText = string.Format("/C python.exe  {0}..\\..\\main.py \"{1}\"",dir,querry);
            System.Diagnostics.Process.Start("CMD.exe", strCmdText);
        }
    }
}