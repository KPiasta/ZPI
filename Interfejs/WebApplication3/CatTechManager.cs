using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication3
{
    public class CatTechManager 
    {
        public enum Category
        {
            Nieznane,
            Realizm,
            Surrealizm,
            Romantyzm,
            Symbolizm,
            Modernizm
        }
        public enum Technique
        {
            Nieznane,
            Olej,
            Akwarela,
            Akryl
        }
        private static Dictionary<String, Category> categories = new Dictionary<string, Category>
        {
            {"NIEZNANE",Category.Nieznane },
            {"REALIZM", Category.Realizm },
            {"REALIŚCI",Category.Realizm },
            {"SURREALIZM", Category.Surrealizm },
            {"SURREALIŚCI",Category.Surrealizm },
            {"ROMANTYZM",Category.Romantyzm },
            {"ROMANTYCY",Category.Romantyzm },
            {"SYMBOLIZM", Category.Symbolizm},
            {"SYMBOLIŚCI",Category.Symbolizm },
            {"MODERNIZM",Category.Modernizm },
            {"MALARZE WSPÓŁCZEŚNI",Category.Modernizm }
        };
        private static Dictionary<String, Technique> techniques = new Dictionary<string, Technique>
        {
            {"NIEZNANE",Technique.Nieznane },
            {"OLEJ", Technique.Olej },
            {"AKWARELA", Technique.Akwarela },
            {"Akryl",Technique.Akryl }
        };
        public static Category getCategoryByName(String name)
        {
            Category cat;
            return categories.TryGetValue(name.ToUpper(), out cat) ? cat : Category.Nieznane;
        }
        public static Technique getTechniqueByName(String name)
        {
            Technique tech;
            return techniques.TryGetValue(name.ToUpper(), out tech) ? tech : Technique.Nieznane;
        }
    }
}