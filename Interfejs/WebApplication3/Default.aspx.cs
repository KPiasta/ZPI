using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class _Default : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            CrawlerManager.runCrawlers("", CrawlerManager.CrawlerMode.list);
            if (!IsPostBack)
                BindList(CrawlerManager.dest);
        }

        private void BindList(String file)
        {
            List<String> results = new List<String>();
            using (StreamReader sr = new StreamReader(file))
            {
                sr.BaseStream.Position = 0;
                sr.DiscardBufferedData();
                String line = null;
                while ((line = sr.ReadLine()) != null)
                {
                    results.Add(line);
                }
            }
            List<MyImage> list = new List<MyImage>();
            int i = 0;
            foreach (String s in results)
            {
                list.Add(new MyImage(i++, "Content/Images/abstract.jpg", s));
            }
            Repeater1.DataSource = list;
            Repeater1.DataBind();

        }


    };

    public class MyImage
    {
        public MyImage(int Id,string Src,string Tit)
        {
        id = Id;
        src = Src;
        title = Tit;
        }
        public int id { get; set; }
        public string src { get; set; }
        public string title { get; set; }
    };

}