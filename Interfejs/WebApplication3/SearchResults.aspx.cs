using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Text.RegularExpressions;

namespace WebApplication3
{
    public class MyImage
    {
        public MyImage(int Id, string Src, string Tit)
        {
            id = Id;
            src = Src;
            title = Tit;
        }
        public int id { get; set; }
        public string src { get; set; }
        public string title { get; set; }
    };
    public partial class SearchResults : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            Uri myUri = new Uri(Request.Url.AbsoluteUri);
            int page;
            var ok=int.TryParse(HttpUtility.ParseQueryString(myUri.Query).Get("page"),out page);
            if (page==0||!ok)
            {
                Message.InnerText = "Witaj! Wyniki twojego wyszukiwania pojawią się tutaj...";
            }
            else
            {
                if (!IsPostBack)
                    BindList(CrawlerManager.dest,CrawlerManager.imgs,0,11);
            }
        }

        private void BindList(String file,String imgFile,int low,int high)
        {
            List<String> results = new List<String>();
            StreamReader sr1 = new StreamReader(file);
            StreamReader sr2 = new StreamReader(imgFile);
            List<MyImage> list = new List<MyImage>();
            sr1.BaseStream.Position = 0;
            sr1.DiscardBufferedData();
            sr2.BaseStream.Position = 0;
            sr2.DiscardBufferedData();
            for (int x = 0; x < low; x++)
            {
                sr1.ReadLine();
            }
            String line1 = null;
            String line2 = null;
            int i = low;

			while ((line1 = sr1.ReadLine()) != null&&(line2 = sr2.ReadLine())!=null&&i++<high)
            {
                list.Add(new MyImage(i, line2,line1));
            }
            Repeater1.DataSource = list;
            Repeater1.DataBind();
			sr1.Close();
			sr2.Close();

        }

        public void resultSelected(object sender, EventArgs e)
        {
            
        }
    };

}