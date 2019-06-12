using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Drawing;

namespace WebApplication3
{
    public partial class Details : Page
    {
        private void LoadData()
        {
            String name = "Nieznane";
            String birth = "Nieznane";
            String birthPlace = "Nieznane";
            String death = "Nieznane";
            String deathPlace = "Nieznane";
            String museum = "Nieznane";
            String education = "Nieznane";
            String wiki = "";
            String magazyn = "";
            List<CatTechManager.Category> cats = new List<CatTechManager.Category>();
            List<CatTechManager.Technique> techs = new List<CatTechManager.Technique>();
            List<String> res = new List<String>();
            Regex rex = new Regex("(?<=<)(.*?)(?=>)");
            Regex rex2 = new Regex(@"\[(.*?)\]");
            String findData(String dataTag, StreamReader sr)
            {
                sr.BaseStream.Position = 0;
                sr.DiscardBufferedData();
                String line = "Nieznane";
                while ((line = sr.ReadLine()) != null)
                {
                    if (line == dataTag)
                    {
                        line = sr.ReadLine();
                        line = rex.Match(line).ToString();
                        break;
                    }
                }
                return line;
            }
            String findRawData(String dataTag, StreamReader sr)
            {
                sr.BaseStream.Position = 0;
                sr.DiscardBufferedData();
                String line = "";
                String result = "";
                while ((line = sr.ReadLine()) != null)
                {
                    if (line == dataTag)
                    {
                        result = dataTag + " ";
                        while (((line = sr.ReadLine()) != "[END]"))
                        {
                            result += line;
                        }
                        break;
                    }
                }
                return result;
            }
            List<String> findAllData(String dataTag, StreamReader sr)
            {
                sr.BaseStream.Position = 0;
                sr.DiscardBufferedData();
                String line = "Nieznane";
                List<String> results = new List<String>();
                while ((line = sr.ReadLine()) != null)
                {
                    if (line == dataTag)
                    {
                        while (((line = sr.ReadLine()) != null) && rex.IsMatch(line))
                        {
                            line = rex.Match(line).ToString();
                            results.Add(line);
                        }
                        break;
                    }
                }
                return results;
            }
            try
            {
                using (StreamReader sr = new StreamReader(CrawlerManager.dest))
                {
                    name = findData("[Name]:", sr);
                    birth = findData("[Birth Date]:", sr);
                    birthPlace = findData("[Birth Place]:", sr);
                    death = findData("[Death Date]:", sr);
                    deathPlace = findData("[Death Place]:", sr);
                    res = findAllData("[Categories]:", sr);
                    foreach(String result in res)
                        cats.Add(CatTechManager.getCategoryByName(result));
                    museum = findData("[Museum]:", sr);
                    education = findData("[Education]:", sr);
                    wiki = findRawData("[wikipedia]:",sr);
                    magazyn = findRawData("[magazyn_sztuki]:", sr);
					sr.Close();
                }
            }
            catch (Exception ex)
            {
                //Well, fuck
            }
            Name.Text = "Imię: " + name +"<br/>";
            Birth.Text = "Urodzony: " + birth + " w " + birthPlace + " <br/>";
            Death.Text = "Zmarł: " + death + " w " + deathPlace +" <br/>";
            Style.Text = "Styl: ";
            foreach (CatTechManager.Category cat in cats)
                Style.Text += Enum.GetName(typeof(CatTechManager.Category), cat) + ", ";
            Style.Text += "<br/>";
            Wiki.Text = wiki;
            Magazyn.Text = magazyn;
        }
        protected void Page_Load(object sender, EventArgs e)
        {
            Uri myUri = new Uri(Request.Url.AbsoluteUri);
            string param = HttpUtility.ParseQueryString(myUri.Query).Get("query");
            CrawlerManager.RunCrawlers(param, CrawlerManager.CrawlerMode.single);
            LoadData();
        }

        protected void Menu1_MenuItemClick(object sender, MenuEventArgs e)
        {
            int i = Int32.Parse(e.Item.Value);
            MultiView1.ActiveViewIndex = i;
            if(Menu1.SelectedItem!=null)
                Menu1.SelectedItem.Selected = false;
            Menu1.Items[i].Selected = true;
        }
    }
}