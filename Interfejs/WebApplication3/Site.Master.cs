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
            var styles = Enum.GetValues(typeof(CatTechManager.Category));
            foreach(CatTechManager.Category s in styles)
            {
                DropDownList1.Items.Add(new ListItem(s.ToString()));
            }
        }


        protected void Button1_Click(object sender, EventArgs e)
        {
            if (TextBox1.Text != "")
            {
                switch (RadioButtonList1.SelectedItem.Text)
                {
                    case "Wyszukaj wg Imienia":
                        CrawlerManager.RunCrawlers(TextBox1.Text, CrawlerManager.CrawlerMode.list);
                        break;
                    case "Wyszukaj wg Dzieła":
                        CrawlerManager.RunCrawlers(TextBox1.Text, CrawlerManager.CrawlerMode.list);
                        break;
                    case "Wyszukaj wg Stylu":
                        CrawlerManager.RunCrawlers(DropDownList1.Text, CrawlerManager.CrawlerMode.category);
                        break;
                }
                CrawlerManager.RunCrawlers("", CrawlerManager.CrawlerMode.images, 0, 11);
                Response.Redirect("SearchResults.aspx?page=1");
            }
        }

        protected void RadioButtonList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch(((RadioButtonList)sender).SelectedItem.Text)
            {
                case "Wyszukaj wg Imienia":
                    TextBox1.Enabled = true;
                    DropDownList1.Enabled = false;
                    break;
                case "Wyszukaj wg Dzieła":
                    TextBox1.Enabled = true;
                    DropDownList1.Enabled = false;
                    break;
                case "Wyszukaj wg Stylu":
                    TextBox1.Enabled = false;
                    DropDownList1.Enabled = false;
                    break;
            }
        }
    }
}