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
            switch(RadioButtonList1.SelectedItem.Text)
            {
                case "Wyszukaj wg Imienia":
                    CrawlerManager.runCrawlers(TextBox1.Text, CrawlerManager.CrawlerMode.list);
                    break;
                case "Wyszukaj wg Dzieła":
                    CrawlerManager.runCrawlers(TextBox1.Text, CrawlerManager.CrawlerMode.list);
                    break;
                case "Wyszukaj wg Stylu":
                    CrawlerManager.runCrawlers(DropDownList1.Text, CrawlerManager.CrawlerMode.category);
                    break;
            }
            
            Response.Redirect("SearchResults.aspx");
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