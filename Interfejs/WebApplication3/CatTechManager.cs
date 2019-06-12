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
            Klasycyzm,
            Romantyzm,
            Symbolizm,
            Modernizm,
            PopArt,
            Abstrakcjonizm,
            Dadaizm,
            Ekspresjonizm,
            Futuryzm,
            Impresjonizm,
            Kubizm,
            Barok,
            Figuratywizm,
            Gotyk,
            Orfizm,
            Renesans,
            Rokoko,
            Secesja,
            Postimpresjonizm,
            Prymitywizm,
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
            {"ABSTRAKCJONIŚCI",Category.Abstrakcjonizm },
            {"ABSTRAKCJONIZM",Category.Abstrakcjonizm },
            {"MALARZE ABSTRAKCJONIZMU",Category.Abstrakcjonizm },
            {"MALARZE ABSTRAKCJONISTYCZNI",Category.Abstrakcjonizm },
            {"DADAIZM",Category.Dadaizm },
            {"DADAISCI",Category.Dadaizm },
            {"MALARZE DADAIZMU", Category.Dadaizm },
            {"MALARZE DADAISTYCZNI" , Category.Dadaizm },
            {"EKSPRESJONIZM",Category.Ekspresjonizm },
            {"EKSPRESJONIŚCI",Category.Ekspresjonizm },
            {"MALARZE EKSPRESJONIZM",Category.Ekspresjonizm },
            {"FUTURYZM",Category.Futuryzm },
            {"FUTURYŚCI",Category.Futuryzm },
            {"MALARZE FUTURYSTYCZNI",Category.Futuryzm },
            {"MALARZE FUTURYZMU",Category.Futuryzm },
            {"IMPRESJONIZM",Category.Impresjonizm },
            {"IMPRESJONIŚCI",Category.Impresjonizm },
            {"MALARZE IMPRESJONISTYCZNI",Category.Impresjonizm },
            {"MALARZE IMPRESJONIZMU",Category.Impresjonizm },
            {"KUBIZM",Category.Kubizm },
            {"KUBIŚCI",Category.Kubizm },
            {"MALARZE KUBISTYCZNI",Category.Kubizm },
            {"MALARZE KUBIZMU",Category.Kubizm },
            {"BAROK",Category.Barok },
            {"MALARZE BAROKU",Category.Barok },
            {"FIGURATYWIZM",Category.Figuratywizm },
            {"MALARZE FIGURATYWISTYCZNI",Category.Figuratywizm },
            {"FIGURATYWIŚCI",Category.Figuratywizm },
            {"MALARZE FIGURATYZMU",Category.Figuratywizm },
            {"GOTYK",Category.Gotyk },
            {"MALARZE GOTYKU",Category.Gotyk },
            {"MALARZE GOTYCCY",Category.Gotyk },
            {"KLASYCYZM",Category.Klasycyzm },
            {"KLASYCYŚCI",Category.Klasycyzm },
            {"MALARZE KLASYCYSTYCZNI",Category.Klasycyzm },
            {"MALARZE KLASYCYZMU",Category.Klasycyzm },
            {"ORFIZM",Category.Orfizm },
            {"ORFIŚCI",Category.Orfizm },
            {"MALARZE ORFIZMU",Category.Orfizm },
            {"RENESANS",Category.Renesans },
            {"MALARZE RENESANSU",Category.Renesans },
            {"ROKOKO",Category.Rokoko },
            {"MALARZE ROKOKO",Category.Rokoko },
            {"SECESJA",Category.Secesja },
            {"MALARZE SECESYJNI",Category.Secesja },
            {"POSTIMPRESJONIZM",Category.Postimpresjonizm },
            {"MALARZE POSTIMPRESJONISTYCZNI",Category.Postimpresjonizm },
            {"POSTIMPRESJONIŚCI",Category.Postimpresjonizm },
            {"MALARZE POSTIMPRESJONIZMU",Category.Postimpresjonizm },
            {"PRYWITYWIZM",Category.Prymitywizm },
            {"PRYWITYWIŚCI",Category.Prymitywizm },
            {"MALARZE PRYWITYWIZMU",Category.Prymitywizm },
            {"MALARZE PRYWITYWISTYCZNI",Category.Prymitywizm },
            {"NIEZNANE",Category.Nieznane },
            {"REALIZM", Category.Realizm },
            {"MALARZE REALIZMU",Category.Realizm },
            {"REALIŚCI",Category.Realizm },
            {"SURREALIZM", Category.Surrealizm },
            {"SURREALIŚCI",Category.Surrealizm },
            {"MALARZE SURREALIZMU",Category.Surrealizm },
            {"ROMANTYZM",Category.Romantyzm },
            {"ROMANTYCY",Category.Romantyzm },
            {"MALARZE ROMANTYCZNI",Category.Romantyzm },
            {"MALARZE ROMANTYZMU",Category.Romantyzm },
            {"SYMBOLIZM", Category.Symbolizm},
            {"SYMBOLIŚCI",Category.Symbolizm },
            {"MALARZE SYMBOLIZMU",Category.Symbolizm },
            {"MODERNIZM",Category.Modernizm },
            {"WSPÓŁCZESNOŚĆ",Category.Modernizm },
            {"MALARZE WSPÓŁCZEŚNI",Category.Modernizm },
            {"KLASYCYZM",Category.Klasycyzm },
            {"MALARZE KLASYCZNI",Category.Klasycyzm },
            {"POPART",Category.PopArt },
            {"MALARZE POPARTU",Category.PopArt }

        };

        public static Category getCategoryByName(String name)
        {
            Category cat;
            return categories.TryGetValue(name.ToUpper(), out cat) ? cat : Category.Nieznane;
        }
    }
}