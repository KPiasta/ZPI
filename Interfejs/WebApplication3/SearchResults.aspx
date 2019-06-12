<%@ Page Title="ResultsPage" Language="C#"  MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="SearchResults.aspx.cs" Inherits="WebApplication3.SearchResults" %>


<asp:Content runat="server" ContentPlaceHolderID="MainContent">
    <style type="text/css">
    #gallery
    {
        
        padding: 10px;
        width: 100%;
        height:100%;
    }
    #gallery ul
    {
        list-style: none;
        display:flex;
        flex-direction:row;
        flex-wrap:wrap;
    }
    #gallery ul li
    {
        display:inline-block;
        height:220px;
    }
    #gallery ul li div
    {
        display: inline-block;
        height:180px;
        width:180px;

    }
    #gallery ul img
    {
        border: 5px solid #3e3e3e;
        border-width: 5px 5px 20px;
    }
    #gallery ul a:hover img
    {
        border: 5px solid #fff;
        border-width: 5px 5px 20px;
        color: #fff;
    }
    #gallery ul a:hover
    {
        color: #fff;
    }
    #pages
    {
        width:70%;
        
        vertical-align:bottom;
        list-style-type:none;
        justify-content:space-between;
        display:flex;
    }
    #pages li
    {
        display:inline-block;
        list-style-type:none;
        float:left;
    }

</style>


    <div >
        <p id="Message" runat="server" style="text-align:center">Wyniki wyszukiwania</p>
        <div id="gallery">
            <asp:Repeater ID="Repeater1" runat="server">
                <HeaderTemplate>
                    <ul>
                        </HeaderTemplate>
                            <ItemTemplate>
                                <li>
                                    <div>

                                        <a runat="server" href='<%# String.Format("Details.aspx?query={0}", Eval("title")) %>' title='<%# Eval("title") %>'>
                                            <div><img src='<%# Eval("src") %>' width="180" height="180" alt=""/></div>
                                            <div style="text-align:center">'<%# Eval("title") %>'</div>
                                        </a>
                                    </div>
                                </a></li>
                            </ItemTemplate>
                        <FooterTemplate>
                    </ul>
                </FooterTemplate>
            </asp:Repeater>
        </div>
        <div style="display:flex;justify-content:center;vertical-align:bottom">
            <ul id="pages" runat="server">
                    <li><a href="SearchResults.aspx?page=1">1</a></li>
                    <li><a href="SearchResults.aspx?page=2">2</a></li>
                    <li><a href="SearchResults.aspx?page=3">3</a></li>
                    <li><a href="SearchResults.aspx?page=4">4</a></li>
                    <li><a href="SearchResults.aspx?page=5">5</a></li>
                    <li><a href="SearchResults.aspx?page=6">6</a></li>
                    <li><a href="SearchResults.aspx?page=7">7</a></li>
                    <li><a href="SearchResults.aspx?page=8">8</a></li>
                    <li><a href="SearchResults.aspx?page=9">9</a></li>

            </ul>
        </div>
    </div>
    
</asp:Content>
