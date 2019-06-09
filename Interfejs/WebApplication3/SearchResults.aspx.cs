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
    public partial class SearchResults : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
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
            foreach(String s in results)
            {
                list.Add(new MyImage(i++, "Content/Images/abstract.jpg", s));
            }
            Repeater1.DataSource = list;
            Repeater1.DataBind();

        }

        public void resultSelected(object sender, EventArgs e)
        {
            
        }
    };

}