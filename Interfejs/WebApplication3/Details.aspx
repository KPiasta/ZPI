<%@ Page Title="DetailsPage" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Details.aspx.cs" Inherits="WebApplication3.Details" %>

<asp:Content ID="DefaultContent" ContentPlaceHolderID="MainContent" runat="server">
        
        <style type="text/css">
            .static
            {
                background-color: var(--inactiveColor)
            }
            .selected
            {
                background-color: var(--activeColor)
            }
        </style>
            <link rel="stylesheet" type="text/css" href="ColorThemes.css">
            <asp:Menu ID="Menu1" runat="server" Orientation="Horizontal" OnMenuItemClick="Menu1_MenuItemClick">
                <staticmenuitemstyle CssClass="static" HorizontalPadding="10px" BorderWidth="2px" BorderColor="Black" BorderStyle="Ridge"/>
                <staticselectedstyle CssClass="selected" HorizontalPadding="10px" BorderWidth="2px" BorderColor="Black" BorderStyle="Ridge"/>
                <Items>
                    <asp:MenuItem Text="Dane osobowe" Value="0" Selected="true"></asp:MenuItem>
                    <asp:MenuItem Text="Kariera i edukacja" Value="1" ></asp:MenuItem>
                    <asp:MenuItem Text="Znane prace" Value="2"></asp:MenuItem>
                </Items>
            </asp:Menu>
        <div class="static" style="height:100%">
            <asp:MultiView ID="MultiView1" runat="server" ActiveViewIndex="0">
                <asp:View ID="Tab1" runat="server">
      
                    <asp:Label ID="Name" runat="server" Font-Size="Large" ></asp:Label>
                    <asp:Label ID="Birth" runat="server" Font-Size="Large"></asp:Label>
                    <asp:Label ID="BirthDate" runat="server" Font-Size="Large"></asp:Label>
                    <asp:Label ID="BirthPlace" runat="server" Font-Size="Large"></asp:Label>
                    <asp:Label ID="Death" runat="server" Font-Size="Large"></asp:Label>
                    <asp:Label ID="DeathPlace" runat="server" Font-Size="Large"></asp:Label>
                    <asp:Label ID="Style" runat="server" Font-Size="Large"></asp:Label>

                </asp:View>
                <asp:View ID="Tab2" runat="server">
                    <asp:Label ID="Magazyn" runat="server"></asp:Label>
                    <br />
                    <asp:Label ID="Wiki" runat="server"></asp:Label>
                </asp:View>
                <asp:View ID="Tab3" runat="server">
                    <p>Znane prace!</p>
                </asp:View>
            </asp:MultiView>
        </div>
</asp:Content>
