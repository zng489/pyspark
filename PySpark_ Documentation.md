```python
# https://medium.com/renato-dantas/temajupyternotebook-f754c065cfe9
!pip install jupyterthemes
from jupyterthemes import get_themes
import jupyterthemes as jt
from jupyterthemes.stylefx import set_nb_theme
set_nb_theme('chesterish')
#jt.get_themes()

#from jupyterthemes.stylefx import set_nb_theme
#set_nb_theme('chesterish')
#!pip list
#!jt -t chesterish -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T

```




<style> div#notebook {
 font-family: sans-serif;
 font-size: 13pt;
 line-height: 170%;
 color: #cdd2e9;
 -webkit-font-smoothing: antialiased !important;
 padding-top: 25px !important;
}
body,
div.body {
 font-family: sans-serif;
 font-size: 13pt;
 color: #a2b0c7;
 background-color: #1a2028;
 background: #1a2028;
 -webkit-font-smoothing: antialiased !important;
}
body.notebook_app {
 padding: 0;
 background-color: #1a2028;
 background: #1a2028;
 padding-right: 0px !important;
 overflow-y: hidden;
}
a {
 font-family: sans-serif;
 color: #a2b0c7;
 -webkit-font-smoothing: antialiased !important;
}
a:hover,
a:focus {
 color: #dbe1ea;
 -webkit-font-smoothing: antialiased !important;
}
div#maintoolbar {
 position: absolute;
 width: 90%;
 margin-left: -10%;
 padding-right: 8%;
 float: left;
 background: transparent !important;
}
#maintoolbar {
 margin-bottom: -3px;
 margin-top: 0px;
 border: 0px;
 min-height: 27px;
 padding-top: 2px;
 padding-bottom: 0px;
}
#maintoolbar .container {
 width: 75%;
 margin-right: auto;
 margin-left: auto;
}
.list_header,
div#notebook_list_header.row.list_header {
 font-size: 14pt;
 color: #dbe1ea;
 background-color: transparent;
 height: 35px;
}
i.fa.fa-folder {
 display: inline-block;
 font: normal normal normal 14px "FontAwesome";
 font-family: "FontAwesome" !important;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 font-size: 18px;
 -moz-osx-font-smoothing: grayscale;
}
#running .panel-group .panel .panel-heading {
 font-size: 14pt;
 color: #a2b0c7;
 padding: 8px 8px;
 background: #252b35;
 background-color: #252b35;
}
#running .panel-group .panel .panel-heading a {
 font-size: 14pt;
 color: #a2b0c7;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
 font-size: 14pt;
 color: #a2b0c7;
}
#running .panel-group .panel .panel-body .list_container .list_item {
 background: #2d3846;
 background-color: #2d3846;
 padding: 2px;
 border-bottom: 2px solid rgba(75,95,118,.30);
}
#running .panel-group .panel .panel-body .list_container .list_item:hover {
 background: #2d3846;
 background-color: #2d3846;
}
#running .panel-group .panel .panel-body {
 padding: 2px;
}
button#refresh_running_list {
 border: none !important;
}
button#refresh_cluster_list {
 border: none !important;
}
div.running_list_info.toolbar_info {
 font-size: 15px;
 padding: 4px 0 4px 0;
 margin-top: 5px;
 margin-bottom: 8px;
 height: 24px;
 line-height: 24px;
 text-shadow: none;
}
.list_placeholder {
 font-weight: normal;
}
#tree-selector {
 padding: 0px;
 border-color: transparent;
}
#project_name > ul > li > a > i.fa.fa-home {
 color: #0b98c8;
 font-size: 17pt;
 display: inline-block;
 position: static;
 padding: 0px 0px;
 font-weight: normal;
 text-align: center;
 vertical-align: text-top;
}
.fa-folder:before {
 color: #4c8be2;
}
.fa-arrow-up:before {
 font-size: 14px;
}
.fa-arrow-down:before {
 font-size: 14px;
}
span#last-modified.btn.btn-xs.btn-default.sort-action:hover .fa,
span#sort-name.btn.btn-xs.btn-default.sort-action:hover .fa {
 color: #009cd1;
}
.folder_icon:before {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f07b";
 color: #4c8be2;
}
.notebook_icon:before {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f02d";
 position: relative;
 color: #48a667 !important;
 top: 0px;
}
.file_icon:before {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f15b";
 position: relative;
 top: 0px;
 color: #92a2bd !important;
}
#project_name a {
 display: inline-flex;
 padding-left: 7px;
 margin-left: -2px;
 text-align: -webkit-auto;
 vertical-align: baseline;
 font-size: 18px;
}
div#notebook_toolbar div.dynamic-instructions {
 font-family: sans-serif;
 font-size: 17px;
 color: #546386;
}
span#login_widget > .button,
#logout {
 font-family: "Proxima Nova", sans-serif;
 color: #a2b0c7;
 background: transparent;
 background-color: transparent;
 border: 2px solid #252e3a;
 font-weight: normal;
 box-shadow: none;
 text-shadow: none;
 border-radius: 3px;
 margin-right: 10px;
 padding: 2px 7px;
}
span#login_widget > .button:hover,
#logout:hover {
 color: #009cd1;
 background-color: transparent;
 background: transparent;
 border: 2px solid #009cd1;
 background-image: none;
 box-shadow: none !important;
 border-radius: 3px;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus,
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
 color: #fefefe;
 background-color: #a2b0c7;
 background: #a2b0c7;
 border-color: #a2b0c7;
 background-image: none;
 box-shadow: none !important;
 border-radius: 2px;
}
body > #header #header-container {
 padding-bottom: 0px;
 padding-top: 4px;
 box-sizing: border-box;
 -moz-box-sizing: border-box;
 -webkit-box-sizing: border-box;
}
body > #header {
 background: #1a2028;
 background-color: #1a2028;
 position: relative;
 z-index: 100;
}
.list_container {
 font-size: 13pt;
 color: #a2b0c7;
 border: none;
 text-shadow: none !important;
}
.list_container > div {
 border-bottom: 1px solid rgba(75,95,118,.30);
 font-size: 13pt;
}
.list_header > div,
.list_item > div {
 padding-top: 6px;
 padding-bottom: 2px;
 padding-left: 0px;
}
.list_header > div .item_link,
.list_item > div .item_link {
 margin-left: -1px;
 vertical-align: middle;
 line-height: 22px;
 font-size: 13pt;
}
.item_icon {
 color: #4c8be2;
 font-size: 13pt;
 vertical-align: middle;
}
.list_item input:not([type="checkbox"]) {
 padding-right: 0px;
 height: 1.75em;
 width: 25%;
 margin: 0px 0 0;
 margin-top: 0px;
}
.list_header > div .item_link,
.list_item > div .item_link {
 margin-left: -1px;
 vertical-align: middle;
 line-height: 1.5em;
 font-size: 12pt;
 display: inline-table;
 position: static;
}
#button-select-all {
 height: 34px;
 min-width: 55px;
 z-index: 0;
 border: none !important;
 padding-top: 0px;
 padding-bottom: 0px;
 margin-bottom: 0px;
 margin-top: 0px;
 left: -3px;
 border-radius: 0px !important;
}
#button-select-all:focus,
#button-select-all:active:focus,
#button-select-all.active:focus,
#button-select-all.focus,
#button-select-all:active.focus,
#button-select-all.active.focus {
 background-color: #252e3a !important;
 background: #252e3a !important;
}
button#tree-selector-btn {
 height: 34px;
 font-size: 12.0pt;
 border: none;
 left: 0px;
 border-radius: 0px !important;
}
input#select-all.pull-left.tree-selector {
 margin-left: 7px;
 margin-right: 2px;
 margin-top: 2px;
 top: 4px;
}
input[type="radio"],
input[type="checkbox"] {
 margin-top: 1px;
 line-height: normal;
}
.delete-button {
 border: none !important;
}
i.fa.fa-trash {
 font-size: 13.5pt;
}
.list_container a {
 font-size: 16px;
 color: #a2b0c7;
 border: none;
 text-shadow: none !important;
 font-weight: normal;
 font-style: normal;
}
div.list_container a:hover {
 color: #dbe1ea;
}
.list_header > div input,
.list_item > div input {
 margin-right: 7px;
 margin-left: 12px;
 vertical-align: baseline;
 line-height: 22px;
 position: relative;
 top: -1px;
}
div.list_item:hover {
 background-color: rgba(75,95,118,.10);
}
.breadcrumb > li {
 font-size: 12.0pt;
 color: #a2b0c7;
 border: none;
 text-shadow: none !important;
}
.breadcrumb > li + li:before {
 content: "/\00a0";
 padding: 0px;
 color: #a2b0c7;
 font-size: 18px;
}
#project_name > .breadcrumb {
 padding: 0px;
 margin-bottom: 0px;
 background-color: transparent;
 font-weight: normal;
 margin-top: -2px;
}
ul#tabs a {
 font-family: sans-serif;
 font-size: 13.5pt;
 font-weight: normal;
 font-style: normal;
 text-shadow: none !important;
}
.nav-tabs {
 font-family: sans-serif;
 font-size: 13.5pt;
 font-weight: normal;
 font-style: normal;
 background-color: transparent;
 border-color: transparent;
 text-shadow: none !important;
 border: 2px solid transparent;
}
.nav-tabs > li > a:active,
.nav-tabs > li > a:focus,
.nav-tabs > li > a:hover,
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:focus,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
 color: #009cd1;
 background-color: transparent;
 border-color: transparent;
 border-bottom: 2px solid transparent;
}
.nav > li.disabled > a,
.nav > li.disabled > a:hover {
 color: #546386;
}
.nav-tabs > li > a:before {
 content: "";
 position: absolute;
 width: 100%;
 height: 2px;
 bottom: -2px;
 left: 0;
 background-color: #009cd1;
 visibility: hidden;
 -webkit-transform: perspective(0)scaleX(0);
 transform: perspective(0)scaleX(0);
 -webkit-transition: ease 220ms;
 transition: ease 220ms;
 -webkit-font-smoothing: antialiased !important;
}
.nav-tabs > li > a:hover:before {
 visibility: visible;
 -webkit-transform: perspective(1)scaleX(1);
 transform: perspective(1)scaleX(1);
}
.nav-tabs > li.active > a:before {
 content: "";
 position: absolute;
 width: 100%;
 height: 2px;
 bottom: -2px;
 left: 0;
 background-color: #009cd1;
 visibility: visible;
 -webkit-transform: perspective(1)scaleX(1);
 transform: perspective(1)scaleX(1);
 -webkit-font-smoothing: subpixel-antialiased !important;
}
div#notebook {
 font-family: sans-serif;
 font-size: 13pt;
 padding-top: 4px;
}
.notebook_app {
 background-color: #1a2028;
}
#notebook-container {
 padding: 13px 2px;
 background-color: #1a2028;
 min-height: 0px;
 box-shadow: none;
 width: 980px;
 margin-right: auto;
 margin-left: auto;
}
div#ipython-main-app.container {
 width: 980px;
 margin-right: auto;
 margin-left: auto;
 margin-right: auto;
 margin-left: auto;
}
.container {
 width: 980px;
 margin-right: auto;
 margin-left: auto;
}
div#menubar-container {
 width: 100%;
 width: 980px;
}
div#header-container {
 width: 980px;
}
.notebook_app #header,
.edit_app #header {
 box-shadow: none !important;
 background-color: #1a2028;
 border-bottom: 2px solid rgba(75,95,118,.30);
}
#header,
.edit_app #header {
 font-family: sans-serif;
 font-size: 13pt;
 box-shadow: none;
 background-color: #1a2028;
}
#header .header-bar,
.edit_app #header .header-bar {
 background: #1a2028;
 background-color: #1a2028;
}
body > #header .header-bar {
 width: 100%;
 background: #1a2028;
}
span.checkpoint_status,
span.autosave_status {
 font-size: small;
 display: none;
}
#menubar,
div#menubar {
 background-color: #1a2028;
 padding-top: 0px !important;
}
#menubar .navbar,
.navbar-default {
 background-color: #1a2028;
 margin-bottom: 0px;
 margin-top: 0px;
}
.navbar {
 border: none;
}
div.navbar-text,
.navbar-text,
.navbar-text.indicator_area,
p.navbar-text.indicator_area {
 margin-top: 8px !important;
 margin-bottom: 0px;
 color: #0b98c8;
}
.navbar-default {
 font-family: sans-serif;
 font-size: 13pt;
 background-color: #1a2028;
 border-color: #323b48;
 line-height: 1.5em;
 padding-bottom: 0px;
}
.navbar-default .navbar-nav > li > a {
 font-family: sans-serif;
 font-size: 13pt;
 color: #a2b0c7;
 display: block;
 line-height: 1.5em;
 padding-top: 14px;
 padding-bottom: 11px;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
 color: #dbe1ea !important;
 background-color: rgba(75,95,118,.30) !important;
 border-color: #323b48 !important;
 line-height: 1.5em;
 transition: 80ms ease;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
 color: #fefefe;
 background-color: #36404e;
 border-color: #36404e;
 line-height: 1.5em;
}
.navbar-nav > li > .dropdown-menu {
 margin-top: 0px;
}
.navbar-nav {
 margin: 0;
}
div.notification_widget.info,
.notification_widget.info,
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:hover,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:focus {
 color: #899ab8 !important;
 background-color: transparent !important;
 border-color: transparent !important;
 padding-bottom: 0px !important;
 margin-bottom: 0px !important;
 font-size: 9pt !important;
 z-index: 0;
}
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn {
 font-size: 9pt !important;
 z-index: 0;
}
.notification_widget {
 color: #4c8be2;
 z-index: -500;
 font-size: 9pt;
 background: transparent;
 background-color: transparent;
 margin-right: 3px;
 border: none;
}
.notification_widget,
div.notification_widget {
 margin-right: 0px;
 margin-left: 0px;
 padding-right: 0px;
 vertical-align: text-top !important;
 margin-top: 6px !important;
 background: transparent !important;
 background-color: transparent !important;
 font-size: 9pt !important;
 border: none;
}
.navbar-btn.btn-xs:hover {
 border: none !important;
 background: transparent !important;
 background-color: transparent !important;
 color: #a2b0c7 !important;
}
div.notification_widget.info,
.notification_widget.info {
 display: none !important;
}
.edit_mode .modal_indicator:before {
 display: none;
}
.command_mode .modal_indicator:before {
 display: none;
}
.item_icon {
 color: #4c8be2;
}
.item_buttons .kernel-name {
 font-size: 13pt;
 color: #4c8be2;
}
.running_notebook_icon:before {
 color: #48a667 !important;
 font: normal normal normal 15px/1 FontAwesome;
 font-size: 15px;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f10c";
 vertical-align: middle;
 position: static;
 display: inherit;
}
.item_buttons .running-indicator {
 padding-top: 4px;
 color: #48a667;
 font-family: sans-serif;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
}
#notification_trusted {
 font-family: sans-serif;
 border: none;
 background: transparent;
 background-color: transparent;
 margin-bottom: 0px !important;
 vertical-align: bottom !important;
 color: #546386 !important;
 cursor: default !important;
}
#notification_area,
div.notification_area {
 float: right !important;
 position: static;
 cursor: pointer;
 padding-top: 6px;
 padding-right: 4px;
}
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn {
 font-size: 9pt !important;
 z-index: 0;
 margin-top: -5px !important;
}
#modal_indicator {
 float: right !important;
 color: #4c8be2;
 background: #1a2028;
 background-color: #1a2028;
 margin-top: 8px !important;
 margin-left: 0px;
}
#kernel_indicator {
 float: right !important;
 color: #0b98c8;
 background: #1a2028;
 background-color: #1a2028;
 border-left: 2px solid #0b98c8;
 padding-top: 0px;
 padding-bottom: 4px;
 margin-top: 10px !important;
 margin-left: -2px;
 padding-left: 5px !important;
}
#kernel_indicator .kernel_indicator_name {
 font-size: 17px;
 color: #0b98c8;
 background: #1a2028;
 background-color: #1a2028;
 padding-left: 5px;
 padding-right: 5px;
 margin-top: 4px;
 vertical-align: text-top;
 padding-bottom: 0px;
}
.kernel_idle_icon:before {
 display: inline-block;
 font: normal normal normal 22px/1 FontAwesome;
 font-size: 22px;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 cursor: pointer;
 margin-left: 0px !important;
 opacity: 0.7;
 vertical-align: bottom;
 margin-top: 1px;
 content: "\f1db";
}
.kernel_busy_icon:before {
 display: inline-block;
 font: normal normal normal 22px/1 FontAwesome;
 font-size: 22px;
 -webkit-animation: pulsate 2s infinite ease-out;
 animation: pulsate 2s infinite ease-out;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 cursor: pointer;
 margin-left: 0px !important;
 vertical-align: bottom;
 margin-top: 1px;
 content: "\f111";
}
@-webkit-keyframes pulsate {
 0% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
 8% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
 50% {
  -webkit-transform: scale(0.75,0.75);
  opacity: 0.3;
 }
 92% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
 100% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
}
div.notification_widget.info,
.notification_widget.info,
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:hover,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:focus {
 color: #899ab8;
 background-color: #1a2028;
 border-color: #1a2028;
}
#notification_area,
div.notification_area {
 float: right !important;
 position: static;
}
.notification_widget,
div.notification_widget {
 margin-right: 0px;
 margin-left: 0px;
 padding-right: 0px;
 vertical-align: text-top !important;
 margin-top: 6px !important;
 z-index: 1000;
}
#kernel_logo_widget,
#kernel_logo_widget .current_kernel_logo {
 display: none;
}
div#ipython_notebook {
 display: none;
}
i.fa.fa-icon {
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 text-rendering: auto;
}
.fa {
 display: inline-block;
 font: normal normal normal 10pt/1 "FontAwesome", sans-serif;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
}
.dropdown-menu {
 font-family: sans-serif;
 font-size: 13pt;
 box-shadow: none;
 padding: 0px;
 text-align: left;
 border: none;
 background-color: #36404e;
 background: #36404e;
 line-height: 1;
}
.dropdown-menu:hover {
 font-family: sans-serif;
 font-size: 13pt;
 box-shadow: none;
 padding: 0px;
 text-align: left;
 border: none;
 background-color: #36404e;
 box-shadow: none;
 line-height: 1;
}
.dropdown-menu > li > a {
 font-family: sans-serif;
 font-size: 12.0pt;
 display: block;
 padding: 10px 20px 9px 10px;
 color: #a2b0c7;
 background-color: #36404e;
 background: #36404e;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
 color: #dbe1ea;
 background-color: #323b48;
 background: #323b48;
 border-color: #323b48;
 transition: 200ms ease;
}
.dropdown-menu .divider {
 height: 1px;
 margin: 0px 0px;
 overflow: hidden;
 background-color: rgba(75,95,118,.55);
}
.dropdown-submenu > .dropdown-menu {
 display: none;
 top: 2px !important;
 left: 100%;
 margin-top: -2px;
 margin-left: 0px;
 padding-top: 0px;
 transition: 200ms ease;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
 font-family: sans-serif;
 font-size: 12.0pt;
 font-weight: normal;
 color: #546386;
 padding: none;
 display: block;
 clear: both;
 white-space: nowrap;
}
.dropdown-submenu > a:after {
 color: #a2b0c7;
 margin-right: -16px;
 margin-top: 0px;
 display: inline-block;
}
.dropdown-submenu:hover > a:after,
.dropdown-submenu:active > a:after,
.dropdown-submenu:focus > a:after,
.dropdown-submenu:visited > a:after {
 color: #0b98c8;
 margin-right: -16px;
 display: inline-block !important;
}
div.kse-dropdown > .dropdown-menu,
.kse-dropdown > .dropdown-menu {
 min-width: 0;
 top: 94%;
}
.btn,
.btn-default {
 font-family: sans-serif;
 color: #a2b0c7;
 background: #252e3a;
 background-color: #252e3a;
 border: 2px solid #252e3a;
 font-weight: normal;
 box-shadow: none;
 text-shadow: none;
 border-radius: 3px;
 font-size: initial;
}
.btn:hover,
.btn:active:hover,
.btn.active:hover,
.btn-default:hover,
.open > .dropdown-toggle.btn-default:hover,
.open > .dropdown-toggle.btn:hover {
 color: #009cd1;
 border: 2px solid #293340;
 background-color: #293340;
 background: #293340;
 background-image: none;
 box-shadow: none !important;
 border-radius: 3px;
}
.btn:active,
.btn.active,
.btn:active:focus,
.btn.active:focus,
.btn:active.focus,
.btn.active.focus,
.btn-default:focus,
.btn-default.focus,
.btn-default:active,
.btn-default.active,
.btn-default:active:hover,
.btn-default.active:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn:focus,
.open > .dropdown-toggle.btn.focus,
.open > .dropdown-toggle.btn-default:hover,
.open > .dropdown-toggle.btn-default:focus,
.open > .dropdown-toggle.btn-default.hover,
.open > .dropdown-toggle.btn-default.focus {
 color: #009cd1;
 border: 2px solid #293340;
 background-color: #293340 !important;
 background: #293340 !important;
 background-image: none;
 box-shadow: none !important;
 border-radius: 3px;
}
.btn-default:active:hover,
.btn-default.active:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.btn-default:active.focus,
.btn-default.active.focus {
 color: #009cd1 !important;
 background-color: #252e3a;
 border-color: #33517c !important;
 transition: 2000ms ease;
}
.btn:focus,
.btn.focus,
.btn:active:focus,
.btn.active:focus,
.btn:active,
.btn.active,
.btn:active.focus,
.btn.active.focus {
 color: #009cd1 !important;
 outline: none !important;
 outline-width: 0px !important;
 background: #33517c !important;
 background-color: #33517c !important;
 border-color: #33517c !important;
 transition: 200ms ease !important;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
 font-size: 13pt;
 background: transparent;
 background-color: transparent;
 border: 0px solid #252b35;
 border-bottom: 2px solid transparent;
 margin-left: 5px;
 padding-top: 4px !important;
}
.item_buttons > .btn:hover,
.item_buttons > .btn-group:hover,
.item_buttons > .input-group:hover,
.item_buttons > .btn.active,
.item_buttons > .btn-group.active,
.item_buttons > .input-group.active,
.item_buttons > .btn.focus {
 margin-left: 5px;
 background: #21262f;
 padding-top: 4px !important;
 background-color: transparent;
 border: 0px solid transparent;
 border-bottom: 2px solid #0b98c8;
 border-radius: 0px;
 transition: none;
}
.item_buttons {
 line-height: 1.5em !important;
}
.item_buttons .btn {
 min-width: 11ex;
}
.btn-group > .btn:first-child {
 margin-left: 3px;
}
.btn-group > .btn-mini,
.btn-sm,
.btn-group-sm > .btn,
.btn-xs,
.btn-group-xs > .btn,
.alternate_upload .btn-upload,
.btn-group,
.btn-group-vertical {
 font-size: inherit;
 font-weight: normal;
 height: inherit;
 line-height: inherit;
}
.btn-xs,
.btn-group-xs > .btn {
 font-size: initial !important;
 background-image: none;
 font-weight: normal;
 text-shadow: none;
 display: inline-table;
 padding: 2px 5px;
 line-height: 1.45;
}
.btn-group > .btn:first-child {
 margin-left: 3px;
}
div#new-buttons > button,
#new-buttons > button,
div#refresh_notebook_list,
#refresh_notebook_list {
 background: transparent;
 background-color: transparent;
 border: none;
}
div#new-buttons > button:hover,
#new-buttons > button:hover,
div#refresh_notebook_list,
#refresh_notebook_list,
div.alternate_upload .btn-upload,
.alternate_upload .btn-upload,
div.dynamic-buttons > button,
.dynamic-buttons > button,
.dynamic-buttons > button:focus,
.dynamic-buttons > button:active:focus,
.dynamic-buttons > button.active:focus,
.dynamic-buttons > button.focus,
.dynamic-buttons > button:active.focus,
.dynamic-buttons > button.active.focus,
#new-buttons > button:focus,
#new-buttons > button:active:focus,
#new-buttons > button.active:focus,
#new-buttons > button.focus,
#new-buttons > button:active.focus,
#new-buttons > button.active.focus,
.alternate_upload .btn-upload:focus,
.alternate_upload .btn-upload:active:focus,
.alternate_upload .btn-upload.active:focus,
.alternate_upload .btn-upload.focus,
.alternate_upload .btn-upload:active.focus,
.alternate_upload .btn-upload.active.focus {
 background: transparent !important;
 background-color: transparent !important;
 border: none !important;
}
.alternate_upload input.fileinput {
 text-align: center;
 vertical-align: bottom;
 margin-left: -.5ex;
 display: inline-table;
 border: solid 0px #252e3a;
 margin-bottom: -1ex;
}
.alternate_upload .btn-upload {
 display: inline-table;
 background: transparent;
 border: none;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
 margin-left: -2px;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
 border-bottom-right-radius: 0;
 border-top-right-radius: 0;
 z-index: 2;
}
.dropdown-header {
 font-family: sans-serif !important;
 font-size: 13pt !important;
 color: #0b98c8 !important;
 border-bottom: none !important;
 padding: 0px !important;
 margin: 6px 6px 0px !important;
}
span#last-modified.btn.btn-xs.btn-default.sort-action,
span#sort-name.btn.btn-xs.btn-default.sort-action,
span#file-size.btn.btn-xs.btn-default.sort-action {
 font-family: sans-serif;
 font-size: 16px;
 background-color: transparent;
 background: transparent;
 border: none;
 color: #a2b0c7;
 padding-bottom: 0px;
 margin-bottom: 0px;
 vertical-align: sub;
}
span#last-modified.btn.btn-xs.btn-default.sort-action {
 margin-left: 19px;
}
button.close {
 border: 0px none;
 font-family: sans-serif;
 font-size: 20pt;
 font-weight: normal;
}
.dynamic-buttons {
 padding-top: 0px;
 display: inline-block;
}
.close {
 color: #dc6972;
 opacity: .5;
 text-shadow: none;
 font-weight: normal;
}
.close:hover {
 color: #dc6972;
 opacity: 1;
 font-weight: normal;
}
div.nbext-enable-btns .btn[disabled],
div.nbext-enable-btns .btn[disabled]:hover,
.btn-default.disabled,
.btn-default[disabled],
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
 color: #92a2bd;
 background: #232c37;
 background-color: #232c37;
 border-color: #232c37;
 transition: 200ms ease;
}
.input-group-addon {
 padding: 2px 5px;
 font-size: 13pt;
 font-weight: normal;
 height: auto;
 color: #a2b0c7;
 text-align: center;
 background-color: transparent;
 border: 2px solid transparent !important;
 text-transform: capitalize;
}
a.btn.btn-default.input-group-addon:hover {
 background: transparent !important;
 background-color: transparent !important;
}
.btn-group > .btn + .dropdown-toggle {
 padding-left: 8px;
 padding-right: 8px;
 height: 100%;
}
.btn-group > .btn + .dropdown-toggle:hover {
 background: #293340 !important;
}
.input-group-btn {
 position: relative;
 font-size: inherit;
 white-space: nowrap;
 background: #252b35;
 background-color: #252b35;
 border: none;
}
.input-group-btn:hover {
 background: #21262f;
 background-color: #21262f;
 border: none;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
 background: #252b35;
 background-color: #252b35;
 border: none;
 margin-left: 2px;
 margin-right: -1px;
 font-size: inherit;
}
.input-group-btn:first-child > .btn:hover,
.input-group-btn:first-child > .btn-group:hover {
 background: #293340;
 background-color: #293340;
 border: none;
 font-size: inherit;
 transition: 200ms ease;
}
div.modal .btn-group > .btn:first-child {
 background: #252b35;
 background-color: #252b35;
 border: 1px solid #232932;
 margin-top: 0px !important;
 margin-left: 0px;
 margin-bottom: 2px;
}
div.modal .btn-group > .btn:first-child:hover {
 background: #21262f;
 background-color: #21262f;
 border: 1px solid #21262f;
 transition: 200ms ease;
}
div.modal > button,
div.modal-footer > button {
 background: #252b35;
 background-color: #252b35;
 border-color: #252b35;
}
div.modal > button:hover,
div.modal-footer > button:hover {
 background: #21262f;
 background-color: #21262f;
 border-color: #21262f;
 transition: 200ms ease;
}
.modal-content {
 font-family: sans-serif;
 font-size: 12.0pt;
 position: relative;
 background: #252b35;
 background-color: #252b35;
 border: none;
 border-radius: 1px;
 background-clip: padding-box;
 outline: none;
}
.modal-header {
 font-family: sans-serif;
 font-size: 13pt;
 color: #a2b0c7;
 background: #252b35;
 background-color: #252b35;
 border-color: rgba(75,95,118,.30);
 padding: 12px;
 min-height: 16.4286px;
}
.modal-content h4 {
 font-family: sans-serif;
 font-size: 16pt;
 color: #a2b0c7;
 padding: 5px;
}
.modal-body {
 background-color: #2d3846;
 position: relative;
 padding: 15px;
}
.modal-footer {
 padding: 8px;
 text-align: right;
 background-color: #2d3846;
 border-top: none;
}
.alert-info {
 background-color: #323f50;
 border-color: rgba(75,95,118,.30);
 color: #a2b0c7;
}
.modal-header .close {
 margin-top: -5px;
 font-size: 25pt;
}
.modal-backdrop,
.modal-backdrop.in {
 opacity: 0.85;
 background-color: notebook-bg;
}
div.panel,
div.panel-default,
.panel,
.panel-default {
 font-family: sans-serif;
 font-size: 13pt;
 background-color: #2d3846;
 color: #a2b0c7;
 margin-bottom: 14px;
 border: 0;
 box-shadow: none;
}
div.panel > .panel-heading,
div.panel-default > .panel-heading {
 font-size: 14pt;
 color: #a2b0c7;
 background: #252b35;
 background-color: #252b35;
 border: 0;
}
.modal .modal-dialog {
 min-width: 950px;
 margin: 50px auto;
}
div.container-fluid {
 margin-right: auto;
 margin-left: auto;
 padding-left: 0px;
 padding-right: 5px;
}
div.form-control,
.form-control {
 font-family: sans-serif;
 font-size: initial;
 color: #a2b0c7;
 background-color: #252b35;
 border: 1px solid #252e3a !important;
 margin-left: 2px;
 box-shadow: none;
 transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s;
}
.form-control-static {
 min-height: inherit;
 height: inherit;
}
.form-group.list-group-item {
 color: #a2b0c7;
 background-color: #2d3846;
 border-color: rgba(75,95,118,.30);
 margin-bottom: 0px;
}
.form-group .input-group {
 float: left;
}
input,
button,
select,
textarea {
 background-color: #252b35;
 font-weight: normal;
 border: 1px solid rgba(75,95,118,.30);
}
select.form-control.select-xs {
 height: 33px;
 font-size: 13pt;
}
.toolbar select,
.toolbar label {
 width: auto;
 vertical-align: middle;
 margin-right: 0px;
 margin-bottom: 0px;
 display: inline;
 font-size: 92%;
 margin-left: 10px;
 padding: 0px;
 background: #252e3a !important;
 background-color: #252e3a !important;
 border: 2px solid #212934 !important;
}
.form-control:focus {
 border-color: #0b98c8;
 outline: 2px solid rgba(0,156,209,.5);
 -webkit-box-shadow: none;
}
::-webkit-input-placeholder {
 color: #546386;
}
::-moz-placeholder {
 color: #546386;
}
:-ms-input-placeholder {
 color: #546386;
}
:-moz-placeholder {
 color: #546386;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
 border: 2px solid rgba(75,95,118,.30) !important;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control:focus {
 border-color: #0b98c8;
 outline: 2px solid rgba(0,156,209,.5);
 -webkit-box-shadow: none;
 box-shadow: none;
}
div.output.output_scroll {
 box-shadow: none;
}
::-webkit-scrollbar {
 width: 11px;
 max-height: 9px;
 background-color: #292d3a;
 border-radius: 3px;
 border: none;
}
::-webkit-scrollbar-track {
 background: #292d3a;
 border: none;
 width: 11px;
 max-height: 9px;
}
::-webkit-scrollbar-thumb {
 border-radius: 2px;
 border: none;
 background: #3f4555;
 background-clip: content-box;
 width: 11px;
}
HTML,
body,
div,
dl,
dt,
dd,
ul,
ol,
li,
h1,
h2,
h3,
h4,
h5,
h6,
pre,
code,
form,
fieldset,
legend,
input,
button,
textarea,
p,
blockquote,
th,
td,
span,
a {
 text-rendering: geometricPrecision;
 -webkit-font-smoothing: subpixel-antialiased;
 font-weight: 400;
}
div.input_area {
 background-color: #293340;
 background: #293340;
 padding-right: 1.2em;
 border: 0px;
 border-radius: 0px;
 border-top-right-radius: 4px;
 border-bottom-right-radius: 4px;
}
div.cell {
 padding: 0px;
 background: #293340;
 background-color: #293340;
 border: medium solid #1a2028;
 border-radius: 4px;
 top: 0;
}
div.cell.selected {
 background: #293340;
 background-color: #293340;
 border: medium solid #1a2028;
 padding: 0px;
 border-radius: 5px;
}
.edit_mode div.cell.selected {
 padding: 0px;
 background: #293340;
 background-color: #293340;
 border: medium solid #1a2028;
 border-radius: 5px;
}
div.cell.edit_mode {
 padding: 0px;
 background: #293340;
 background-color: #293340;
}
div.CodeMirror-sizer {
 margin-left: 0px;
 margin-bottom: -21px;
 border-right-width: 16px;
 min-height: 37px;
 padding-right: 0px;
 padding-bottom: 0px;
 margin-top: 0px;
}
div.cell.selected:before,
.edit_mode div.cell.selected:before,
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
 background: #293340 !important;
 border: none;
 border-radius: 3px;
 position: absolute;
 display: block;
 top: 0px;
 left: 0px;
 width: 0px;
 height: 100%;
}
div.cell.text_cell.selected::before,
.edit_mode div.cell.text_cell.selected:before,
div.cell.text_cell.selected:before,
div.cell.text_cell.selected.jupyter-soft-selected:before {
 background: #293340 !important;
 background-color: #293340 !important;
 border-color: #0b98c8 !important;
}
div.cell.code_cell .input {
 border-left: 5px solid #293340 !important;
 border-radius: 3px;
 border-bottom-left-radius: 3px;
 border-top-left-radius: 3px;
}
div.cell.code_cell.selected .input {
 border-left: 5px solid #008ebf !important;
 border-radius: 3px;
}
.edit_mode div.cell.code_cell.selected .input {
 border-left: 5px solid #005573 !important;
 border-radius: 3px;
}
.edit_mode div.cell.selected:before {
 height: 100%;
 border-left: 5px solid #005573 !important;
 border-radius: 3px;
}
div.cell.jupyter-soft-selected,
div.cell.selected.jupyter-soft-selected {
 border-left-color: #005573 !important;
 border-left-width: 0px !important;
 padding-left: 7px !important;
 border-right-color: #005573 !important;
 border-right-width: 0px !important;
 background: #005573 !important;
 border-radius: 6px !important;
}
div.cell.selected.jupyter-soft-selected .input {
 border-left: 5px solid #293340 !important;
}
div.cell.selected.jupyter-soft-selected {
 border-left-color: #008ebf;
 border-color: #1a2028;
 padding-left: 7px;
 border-radius: 6px;
}
div.cell.code_cell.selected .input {
 border-left: none;
 border-radius: 3px;
}
div.cell.selected.jupyter-soft-selected .prompt,
div.cell.text_cell.selected.jupyter-soft-selected .prompt {
 top: 0;
 border-left: #293340 !important;
 border-radius: 2px;
}
div.cell.text_cell.selected.jupyter-soft-selected .input_prompt {
 border-left: none !important;
}
div.cell.text_cell.jupyter-soft-selected,
div.cell.text_cell.selected.jupyter-soft-selected {
 border-left-color: #005573 !important;
 border-left-width: 0px !important;
 padding-left: 26px !important;
 border-right-color: #005573 !important;
 border-right-width: 0px !important;
 background: #005573 !important;
 border-radius: 5px !important;
}
div.cell.jupyter-soft-selected .input,
div.cell.selected.jupyter-soft-selected .input {
 border-left-color: #005573 !important;
}
div.prompt,
.prompt {
 font-family: monospace, monospace;
 font-size: 9pt !important;
 font-weight: normal;
 color: #546386;
 line-height: 170%;
 padding: 0px;
 padding-top: 4px;
 padding-left: 0px;
 padding-right: 1px;
 text-align: right !important;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
}
div.prompt.input_prompt {
 font-size: 9pt !important;
 background-color: #293340;
 border-top: 0px;
 border-top-right-radius: 0px;
 border-bottom-left-radius: 0px;
 border-bottom-right-radius: 0px;
 padding-right: 3px;
 min-width: 11.5ex;
 width: 11.5ex !important;
}
div.cell.code_cell .input_prompt {
 border-right: 2px solid rgba(0,156,209,.5);
}
div.cell.selected .prompt {
 top: 0;
}
.edit_mode div.cell.selected .prompt {
 top: 0;
}
.edit_mode div.cell.selected .prompt {
 top: 0;
}
.run_this_cell {
 visibility: hidden;
 color: transparent;
 padding-top: 0px;
 padding-bottom: 0px;
 padding-left: 3px;
 padding-right: 12px;
 width: 1.5ex;
 width: 0ex;
 background: transparent;
 background-color: transparent;
}
div.code_cell:hover div.input .run_this_cell {
 visibility: visible;
}
div.cell.code_cell.rendered.selected .run_this_cell:hover {
 background-color: #212934;
 background: #212934;
 color: #008ebf !important;
}
div.cell.code_cell.rendered.unselected .run_this_cell:hover {
 background-color: #212934;
 background: #212934;
 color: #008ebf !important;
}
i.fa-step-forward.fa {
 display: inline-block;
 font: normal normal normal 9px "FontAwesome";
}
.fa-step-forward:before {
 content: "\f04b";
}
div.cell.selected.jupyter-soft-selected .run_this_cell,
div.cell.selected.jupyter-soft-selected .run_this_cell:hover,
div.cell.unselected.jupyter-soft-selected .run_this_cell:hover,
div.cell.code_cell.rendered.selected.jupyter-soft-selected .run_this_cell:hover,
div.cell.code_cell.rendered.unselected.jupyter-soft-selected .run_this_cell:hover {
 background-color: #005573 !important;
 background: #005573 !important;
 color: #005573 !important;
}
div.output_wrapper {
 background-color: #323a48;
 border: 0px;
 left: 0px;
 margin-bottom: 0em;
 margin-top: 0em;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
}
div.output_subarea.output_text.output_stream.output_stdout,
div.output_subarea.output_text {
 font-family: monospace, monospace;
 font-size: 8.5pt !important;
 line-height: 150% !important;
 background-color: #323a48;
 color: #b4bcde;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 margin-left: 11.5px;
}
div.output_area pre {
 font-family: monospace, monospace;
 font-size: 8.5pt !important;
 line-height: 151% !important;
 color: #b4bcde;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
}
div.output_area {
 display: -webkit-box;
}
div.output_html {
 font-family: monospace, monospace;
 font-size: 8.5pt;
 color: #e2e5f2;
 background-color: #323a48;
 background: #323a48;
}
div.output_subarea {
 overflow-x: auto;
 padding: 1.2em !important;
 -webkit-box-flex: 1;
 -moz-box-flex: 1;
 box-flex: 1;
 flex: 1;
}
div.btn.btn-default.output_collapsed {
 background: #1b1f26;
 background-color: #1b1f26;
 border-color: #1b1f26;
}
div.btn.btn-default.output_collapsed:hover {
 background: #161a20;
 background-color: #161a20;
 border-color: #161a20;
}
div.prompt.output_prompt {
 font-family: monospace, monospace;
 font-weight: bold !important;
 background-color: #323a48;
 color: transparent;
 border-bottom-left-radius: 4px;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 border-bottom-right-radius: 0px;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
 border-right: 2px solid transparent;
}
div.out_prompt_overlay.prompt {
 font-family: monospace, monospace;
 font-weight: bold !important;
 background-color: #323a48;
 border-bottom-left-radius: 2px;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 border-bottom-right-radius: 0px;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
 border-right: 2px solid transparent;
 color: transparent;
}
div.out_prompt_overlay.prompt:hover {
 background-color: #374556;
 box-shadow: none !important;
 border: none;
 border-bottom-left-radius: 2px;
 -webkit-border-: 2px;
 -moz-border-radius: 2px;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
 border-right: 2px solid #374556 !important;
}
div.cell.code_cell .output_prompt {
 border-right: 2px solid transparent;
 color: transparent;
}
div.cell.selected .output_prompt,
div.cell.selected .out_prompt_overlay.prompt {
 border-left: 5px solid #005573;
 border-right: 2px solid #323a48;
 border-radius: 0px !important;
}
.edit_mode div.cell.selected .output_prompt,
.edit_mode div.cell.selected .out_prompt_overlay.prompt {
 border-left: 5px solid #005573;
 border-right: 2px solid #323a48;
 border-radius: 0px !important;
}
div.text_cell,
div.text_cell_render pre,
div.text_cell_render {
 font-family: sans-serif;
 font-size: 13pt;
 line-height: 130% !important;
 color: #b0bdd7;
 background: #293340;
 background-color: #293340;
 border-radius: 0px;
}
div .text_cell_render {
 padding: 0.4em 0.4em 0.4em 0.4em;
}
div.cell.text_cell .CodeMirror-lines {
 padding-top: .7em !important;
 padding-bottom: .4em !important;
 padding-left: .5em !important;
 padding-right: .5em !important;
 margin-top: .4em;
 margin-bottom: .3em;
}
div.cell.text_cell.unrendered div.input_area,
div.cell.text_cell.rendered div.input_area {
 background-color: #293340;
 background: #293340;
 border: 0px;
 border-radius: 2px;
}
div.cell.text_cell .CodeMirror,
div.cell.text_cell .CodeMirror pre {
 line-height: 170% !important;
}
div.cell.text_cell.rendered.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #293340;
 background-color: #293340;
 border-radius: 0px;
}
div.cell.text_cell.unrendered.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #293340;
 background-color: #293340;
 border-radius: 0px;
}
div.cell.text_cell.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #293340;
 background-color: #293340;
 border-radius: 0px;
}
.edit_mode div.cell.text_cell.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #293340;
 background-color: #293340;
 border-radius: 0px;
}
div.text_cell.unrendered,
div.text_cell.unrendered.selected,
div.edit_mode div.text_cell.unrendered {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #293340;
 background-color: #293340;
 border-radius: 0px;
}
div.cell.text_cell .prompt {
 border-right: 0;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
}
div.cell.text_cell.rendered .prompt {
 font-family: monospace, monospace;
 font-size: 9.5pt !important;
 font-weight: normal;
 color: #546386 !important;
 text-align: right !important;
 min-width: 14.5ex !important;
 width: 14.5ex !important;
 background-color: #293340;
 border-right: 2px solid rgba(0,156,209,.5);
 border-left: 4px solid #293340;
}
div.cell.text_cell.unrendered .prompt {
 font-family: monospace, monospace;
 font-size: 9.5pt !important;
 font-weight: normal;
 color: #546386 !important;
 text-align: right !important;
 min-width: 14.5ex !important;
 width: 14.5ex !important;
 border-right: 2px solid rgba(0,156,209,.5);
 border-left: 4px solid #293340;
 background-color: #293340;
}
div.cell.text_cell.rendered .prompt {
 border-right: 2px solid rgba(0,156,209,.5);
}
div.cell.text_cell.rendered.selected .prompt {
 top: 0;
 border-left: 4px solid #0b98c8;
 border-right: 2px solid rgba(0,156,209,.5);
}
div.text_cell.unrendered.selected .prompt,
div.text_cell.rendered.selected .prompt {
 top: 0;
 background: #293340;
 border-left: 4px solid #005573;
 border-right: 2px solid rgba(0,156,209,.5);
}
div.rendered_html code {
 font-family: monospace, monospace;
 font-size: 11pt;
 padding-top: 3px;
 padding-left: 2px;
 color: #cdd2e9;
 background: #252e3a;
 background-color: #252e3a;
}
pre,
code,
kbd,
samp {
 white-space: pre-wrap;
}
.well code,
code {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 line-height: 170% !important;
 color: #b0bdd7;
 background: #252e3a;
 background-color: #252e3a;
 border-color: #252e3a;
}
kbd {
 padding: 1px;
 font-size: 11pt;
 font-weight: 800;
 color: #cdd2e9;
 background-color: transparent !important;
 border: 0;
 box-shadow: none;
}
pre {
 display: block;
 padding: 8.5px;
 margin: 0 0 9px;
 font-size: 12.0pt;
 line-height: 1.42857143;
 color: #cdd2e9;
 background-color: #252e3a;
 border: 1px solid #252e3a;
 border-radius: 2px;
}
div.rendered_html {
 color: #b0bdd7;
}
.rendered_html * + ul {
 margin-top: .4em;
 margin-bottom: .3em;
}
.rendered_html * + p {
 margin-top: .5em;
 margin-bottom: .5em;
}
div.rendered_html pre {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 line-height: 170% !important;
 color: #b0bdd7 !important;
 background: #252e3a;
 background-color: #252e3a;
 max-width: 80%;
 border-radius: 0px;
 border-left: 3px solid #252e3a;
 max-width: 80%;
 border-radius: 0px;
 padding-left: 5px;
 margin-left: 6px;
}
div.text_cell_render pre,
div.text_cell_render code {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 line-height: 170% !important;
 color: #b0bdd7;
 background: #1a2028;
 background-color: #1a2028;
 max-width: 80%;
 border-radius: 0px;
 border-left: none;
}
div.text_cell_render pre {
 border-left: 3px solid rgba(0,156,209,.5) !important;
 max-width: 80%;
 border-radius: 0px;
 padding-left: 5px;
 margin-left: 6px;
}
div.text_cell_render h1,
div.rendered_html h1,
div.text_cell_render h2,
div.rendered_html h2,
div.text_cell_render h3,
div.rendered_html h3,
div.text_cell_render h4,
div.rendered_html h4,
div.text_cell_render h5,
div.rendered_html h5 {
 font-family: sans-serif;
 margin: 0.4em .2em .3em .2em !important;
}
.rendered_html h1:first-child,
.rendered_html h2:first-child,
.rendered_html h3:first-child,
.rendered_html h4:first-child,
.rendered_html h5:first-child,
.rendered_html h6:first-child {
 margin-top: 0.2em !important;
 margin-bottom: 0.2em !important;
}
.rendered_html h1,
.text_cell_render h1 {
 color: #0b98c8 !important;
 font-size: 200%;
 text-align: left;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h2,
.text_cell_render h2 {
 color: #0b98c8 !important;
 font-size: 170%;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h3,
.text_cell_render h3 {
 color: #0b98c8 !important;
 font-size: 140%;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h4,
.text_cell_render h4 {
 color: #0b98c8 !important;
 font-size: 110%;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h5,
.text_cell_render h5 {
 color: #0b98c8 !important;
 font-size: 100%;
 font-style: normal;
 font-weight: normal;
}
hr {
 margin-top: 8px;
 margin-bottom: 10px;
 border: 0;
 border-top: 1px solid #0b98c8;
}
.rendered_html hr {
 color: #0b98c8;
 background-color: #0b98c8;
 margin-right: 2em;
}
#complete > select > option:hover {
 background: #323b48;
 background-color: #323b48;
}
div#_vivaldi-spatnav-focus-indicator._vivaldi-spatnav-focus-indicator {
 position: absolute;
 z-index: 9999999999;
 top: 0px;
 left: 0px;
 box-shadow: none;
 pointer-events: none;
 border-radius: 2px;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
 text-align: left;
 vertical-align: middle;
 padding: 0.42em 0.47em;
 line-height: normal;
 white-space: normal;
 max-width: none;
 border: none;
}
.rendered_html td {
 font-family: sans-serif !important;
 font-size: 9.3pt;
}
.rendered_html table {
 font-family: sans-serif !important;
 margin-left: 8px;
 margin-right: auto;
 border: none;
 border-collapse: collapse;
 border-spacing: 0;
 color: #e2e5f2;
 table-layout: fixed;
}
.rendered_html thead {
 font-family: sans-serif !important;
 font-size: 10.3pt !important;
 background: #27313d;
 color: #bbc2e1;
 border-bottom: 1px solid #27313d;
 vertical-align: bottom;
}
.rendered_html tbody tr:nth-child(odd) {
 background: #3f495a;
}
.rendered_html tbody tr {
 background: #394251;
}
.rendered_html tbody tr:hover:nth-child(odd) {
 background: #3d4757;
}
.rendered_html tbody tr:hover {
 background: #373f4e;
}
.rendered_html * + table {
 margin-top: .05em;
}
div.widget-area {
 background-color: #323a48;
 background: #323a48;
 color: #b4bcde;
}
div.widget-area a {
 font-family: sans-serif;
 font-size: 12.0pt;
 font-weight: normal;
 font-style: normal;
 color: #a2b0c7;
 text-shadow: none !important;
}
div.widget-area a:hover,
div.widget-area a:focus {
 font-family: sans-serif;
 font-size: 12.0pt;
 font-weight: normal;
 font-style: normal;
 color: #dbe1ea;
 background: rgba(75,95,118,.30);
 background-color: rgba(75,95,118,.30);
 border-color: transparent;
 background-image: none;
 text-shadow: none !important;
}
div.widget_item.btn-group > button.btn.btn-default.widget-combo-btn,
div.widget_item.btn-group > button.btn.btn-default.widget-combo-btn:hover {
 background: #232932;
 background-color: #232932;
 border: 2px solid #232932 !important;
 font-size: inherit;
 z-index: 0;
}
div.jupyter-widgets.widget-hprogress.widget-hbox {
 display: inline-table !important;
 width: 38% !important;
 margin-left: 10px;
}
div.jupyter-widgets.widget-hprogress.widget-hbox .widget-label,
div.widget-hbox .widget-label,
.widget-hbox .widget-label,
.widget-inline-hbox .widget-label,
div.widget-label {
 text-align: -webkit-auto !important;
 margin-left: 15px !important;
 max-width: 240px !important;
 min-width: 100px !important;
 vertical-align: text-top !important;
 color: #b4bcde !important;
 font-size: 14px !important;
}
.widget-hprogress .progress {
 flex-grow: 1;
 height: 20px;
 margin-top: auto;
 margin-left: 12px;
 margin-bottom: auto;
 width: 300px;
}
.progress {
 overflow: hidden;
 height: 22px;
 margin-bottom: 10px;
 padding-left: 10px;
 background-color: #4a5569 !important;
 border-radius: 2px;
 -webkit-box-shadow: none;
 box-shadow: none;
 z-index: 10;
}
.progress-bar-danger {
 background-color: #e74c3c !important;
}
.progress-bar-info {
 background-color: #3498db !important;
}
.progress-bar-warning {
 background-color: #ff914d !important;
}
.progress-bar-success {
 background-color: #83a83b !important;
}
.widget-select select {
 margin-left: 12px;
}
.rendered_html :link {
 font-family: sans-serif;
 font-size: 100%;
 color: #0b98c8;
 text-decoration: underline;
}
.rendered_html :visited,
.rendered_html :visited:active,
.rendered_html :visited:focus {
 color: #12a3d6;
}
.rendered_html :visited:hover,
.rendered_html :link:hover {
 font-family: sans-serif;
 font-size: 100%;
 color: #0080aa;
}
div.cell.text_cell a.anchor-link:link {
 font-size: inherit;
 text-decoration: none;
 padding: 0px 20px;
 visibility: none;
 color: rgba(0,0,0,.32);
}
div.cell.text_cell a.anchor-link:link:hover {
 font-size: inherit;
 color: #0dc1ff;
}
.navbar-text {
 margin-top: 4px;
 margin-bottom: 0px;
}
#clusters > a {
 color: #51c0ef;
 text-decoration: underline;
 cursor: auto;
}
#clusters > a:hover {
 color: #4c8be2;
 text-decoration: underline;
 cursor: auto;
}
#nbextensions-configurator-container > div.row.container-fluid.nbext-selector > h3 {
 font-size: 17px;
 margin-top: 5px;
 margin-bottom: 8px;
 height: 24px;
 padding: 4px 0 4px 0;
}
div#nbextensions-configurator-container.container,
#nbextensions-configurator-container.container {
 width: 100%;
 margin-right: auto;
 margin-left: auto;
}
div.nbext-selector > nav > .nav > li > a {
 font-family: sans-serif;
 font-size: 10.5pt;
 padding: 2px 5px;
}
div.nbext-selector > nav > .nav > li > a:hover {
 background: transparent;
}
div.nbext-selector > nav > .nav > li:hover {
 background-color: rgba(75,95,118,.30) !important;
 background: rgba(75,95,118,.30) !important;
}
div.nbext-selector > nav > .nav > li.active:hover {
 background: transparent !important;
 background-color: transparent !important;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:active,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
 color: #fefefe;
 background-color: rgba(75,95,118,.30) !important;
 background: rgba(75,95,118,.30) !important;
 -webkit-backface-visibility: hidden;
 -webkit-font-smoothing: subpixel-antialiased !important;
}
div.nbext-readme > .nbext-readme-contents > .rendered_html {
 font-family: sans-serif;
 font-size: 11.5pt;
 line-height: 145%;
 padding: 1em 1em;
 color: #b0bdd7;
 background-color: #293340;
 -webkit-box-shadow: none;
 -moz-box-shadow: none;
 box-shadow: none;
}
.nbext-icon,
.nbext-desc,
.nbext-compat-div,
.nbext-enable-btns,
.nbext-params {
 margin-bottom: 8px;
 font-size: 11.5pt;
}
div.nbext-readme > .nbext-readme-contents {
 padding: 0;
 overflow-y: hidden;
}
div.nbext-readme > .nbext-readme-contents:not(:empty) {
 margin-top: 0.5em;
 margin-bottom: 2em;
 border: none;
 border-top-color: rgba(0,156,209,.3);
}
.nbext-showhide-incompat {
 padding-bottom: 0.5em;
 color: #92a2bd;
 font-size: 10.5pt;
}
.nbext-filter-menu.dropdown-menu > li > a:hover,
.nbext-filter-menu.dropdown-menu > li > a:focus,
.nbext-filter-menu.dropdown-menu > li > a.ui-state-focus {
 color: #dbe1ea !important;
 background-color: #323b48 !important;
 background: #323b48 !important;
 border-color: #323b48 !important;
}
.nbext-filter-input-wrap > .nbext-filter-input-subwrap,
.nbext-filter-input-wrap > .nbext-filter-input-subwrap > input {
 border: none;
 outline: none;
 background-color: transparent;
 padding: 0;
 vertical-align: middle;
 margin-top: -2px;
}
span.rendered_html code {
 background-color: transparent;
 color: #a2b0c7;
}
#nbextensions-configurator-container > div.row.container-fluid.nbext-selector {
 padding-left: 0px;
 padding-right: 0px;
}
.nbext-filter-menu {
 max-height: 55vh !important;
 overflow-y: auto;
 outline: none;
 border: none;
}
.nbext-filter-menu:hover {
 border: none;
}
.alert-warning {
 background-color: #2d3846;
 border-color: #2d3846;
 color: #a2b0c7;
}
.notification_widget.danger {
 color: #ffffff;
 background-color: #e74c3c;
 border-color: #e74c3c;
 padding-right: 5px;
}
#nbextensions-configurator-container > div.nbext-buttons.tree-buttons.no-padding.pull-right > span > button {
 border: none !important;
}
button#refresh_running_list {
 border: none !important;
}
mark,
.mark {
 background-color: #293340;
 color: #b0bdd7;
 padding: .15em;
}
a.text-warning,
a.text-warning:hover {
 color: #546386;
}
a.text-warning.bg-warning {
 background-color: #1a2028;
}
span.bg-success.text-success {
 background-color: transparent;
 color: #48a667;
}
span.bg-danger.text-danger {
 background-color: #1a2028;
 color: #dc6972;
}
.has-success .input-group-addon {
 color: #48a667;
 border-color: transparent;
 background: inherit;
 background-color: rgba(83,180,115,.10);
}
.has-success .form-control {
 border-color: #48a667;
 -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
 box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
}
.has-error .input-group-addon {
 color: #dc6972;
 border-color: transparent;
 background: inherit;
 background-color: rgba(192,57,67,.10);
}
.has-error .form-control {
 border-color: #dc6972;
 -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
 box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
}
.kse-input-group-pretty > kbd {
 font-family: monospace, monospace;
 color: #a2b0c7;
 font-weight: normal;
 background: transparent;
}
.kse-input-group-pretty > kbd {
 font-family: monospace, monospace;
 color: #a2b0c7;
 font-weight: normal;
 background: transparent;
}
div.nbext-enable-btns .btn[disabled],
div.nbext-enable-btns .btn[disabled]:hover,
.btn-default.disabled,
.btn-default[disabled] {
 background: #232c37;
 background-color: #232c37;
 color: #98a8c1;
}
label#Keyword-Filter {
 display: none;
}
.input-group .nbext-list-btn-add,
.input-group-btn:last-child > .btn-group > .btn {
 background: #252b35;
 background-color: #252b35;
 border-color: #252b35;
 border: 2px solid #252b35;
}
.input-group .nbext-list-btn-add:hover,
.input-group-btn:last-child > .btn-group > .btn:hover {
 background: #21262f;
 background-color: #21262f;
 border-color: #21262f;
 border: 2px solid #21262f;
}
#notebook-container > div.cell.code_cell.rendered.selected > div.widget-area > div.widget-subarea > div > div.widget_item.btn-group > button.btn.btn-default.dropdown-toggle.widget-combo-carrot-btn {
 background: #252b35;
 background-color: #252b35;
 border-color: #252b35;
}
#notebook-container > div.cell.code_cell.rendered.selected > div.widget-area > div.widget-subarea > div > div.widget_item.btn-group > button.btn.btn-default.dropdown-toggle.widget-combo-carrot-btn:hover {
 background: #21262f;
 background-color: #21262f;
 border-color: #21262f;
}
.ui-widget-content {
 background: #252e3a;
 background-color: #252e3a;
 border: 2px solid #252e3a;
 color: #a2b0c7;
}
div.collapsible_headings_toggle {
 color: rgba(75,95,118,.55) !important;
}
div.collapsible_headings_toggle:hover {
 color: #0b98c8 !important;
}
.collapsible_headings_toggle .h1,
.collapsible_headings_toggle .h2,
.collapsible_headings_toggle .h3,
.collapsible_headings_toggle .h4,
.collapsible_headings_toggle .h5,
.collapsible_headings_toggle .h6 {
 margin: 0.3em .4em 0em 0em !important;
 line-height: 1.2 !important;
}
div.collapsible_headings_toggle .fa-caret-down:before,
div.collapsible_headings_toggle .fa-caret-right:before {
 font-size: xx-large;
 transition: transform 1000ms;
 transform: none !important;
}
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h1:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h2:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h3:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h4:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h5:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h6:after {
 position: absolute;
 right: 0;
 bottom: 20% !important;
 content: "[\002026]";
 color: rgba(75,95,118,.55) !important;
 padding: 0.5em 0em 0em 0em !important;
}
.collapsible_headings_ellipsis .rendered_html h1,
.collapsible_headings_ellipsis .rendered_html h2,
.collapsible_headings_ellipsis .rendered_html h3,
.collapsible_headings_ellipsis .rendered_html h4,
.collapsible_headings_ellipsis .rendered_html h5,
.collapsible_headings_ellipsis .rendered_html h6,
.collapsible_headings_toggle .fa {
 transition: transform 1000ms !important;
 -webkit-transform: inherit !important;
 -moz-transform: inherit !important;
 -ms-transform: inherit !important;
 -o-transform: inherit !important;
 transform: inherit !important;
 padding-right: 0px !important;
}
#toc-wrapper {
 z-index: 90;
 position: fixed !important;
 display: flex;
 flex-direction: column;
 overflow: hidden;
 padding: 10px;
 border-style: solid;
 border-width: thin;
 border-right-width: medium !important;
 background-color: #1a2028 !important;
}
#toc-wrapper.ui-draggable.ui-resizable.sidebar-wrapper {
 border-color: rgba(75,95,118,.30) !important;
}
#toc a,
#navigate_menu a,
.toc {
 color: #a2b0c7 !important;
 font-size: 11pt !important;
}
#toc li > span:hover {
 background-color: #323b48 !important;
}
#toc a:hover,
#navigate_menu a:hover,
.toc {
 color: #fefefe !important;
 font-size: 11pt !important;
}
#toc-wrapper .toc-item-num {
 color: #0b98c8 !important;
 font-size: 11pt !important;
}
input.raw_input {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 color: #cdd2e9;
 background-color: #252e3a;
 border-color: #232c37;
 background: #232c37;
 width: auto;
 vertical-align: baseline;
 padding: 0em 0.25em;
 margin: 0em 0.25em;
 -webkit-box-shadow: none;
 box-shadow: none;
}
audio,
video {
 display: inline;
 vertical-align: middle;
 align-content: center;
 margin-left: 20%;
}
.cmd-palette .modal-body {
 padding: 0px;
 margin: 0px;
}
.cmd-palette form {
 background: #293547;
 background-color: #293547;
}
.typeahead-field input:last-child,
.typeahead-hint {
 background: #293547;
 background-color: #293547;
 z-index: 1;
}
.typeahead-field input {
 font-family: sans-serif;
 color: #cdd2e9;
 border: none;
 font-size: 28pt;
 display: inline-block;
 line-height: inherit;
 padding: 3px 10px;
 height: 70px;
}
.typeahead-select {
 background-color: #293547;
}
body > div.modal.cmd-palette.typeahead-field {
 display: table;
 border-collapse: separate;
 background-color: #2b3850;
}
.typeahead-container button {
 font-family: sans-serif;
 font-size: 28pt;
 background-color: #252b35;
 border: none;
 display: inline-block;
 line-height: inherit;
 padding: 3px 10px;
 height: 70px;
}
.typeahead-search-icon {
 min-width: 40px;
 min-height: 55px;
 display: block;
 vertical-align: middle;
 text-align: center;
}
.typeahead-container button:focus,
.typeahead-container button:hover {
 color: #dbe1ea;
 background-color: #21262f;
 border-color: #293340;
}
.typeahead-list > li.typeahead-group.active > a,
.typeahead-list > li.typeahead-group > a,
.typeahead-list > li.typeahead-group > a:focus,
.typeahead-list > li.typeahead-group > a:hover {
 display: none;
}
.typeahead-dropdown > li > a,
.typeahead-list > li > a {
 color: #a2b0c7;
 text-decoration: none;
}
.typeahead-dropdown,
.typeahead-list {
 font-family: sans-serif;
 font-size: 13pt;
 color: #a2b0c7;
 background-color: #202937;
 border: none;
 background-clip: padding-box;
 margin-top: 0px;
 padding: 3px 2px 3px 0px;
 line-height: 1.7;
}
.typeahead-dropdown > li.active > a,
.typeahead-dropdown > li > a:focus,
.typeahead-dropdown > li > a:hover,
.typeahead-list > li.active > a,
.typeahead-list > li > a:focus,
.typeahead-list > li > a:hover {
 color: #dbe1ea;
 background-color: #2b3850;
 border-color: #2b3850;
}
.command-shortcut:before {
 content: "(command)";
 padding-right: 3px;
 color: #546386;
}
.edit-shortcut:before {
 content: "(edit)";
 padding-right: 3px;
 color: #546386;
}
ul.typeahead-list i {
 margin-left: 1px;
 width: 18px;
 margin-right: 10px;
}
ul.typeahead-list {
 max-height: 50vh;
 overflow: auto;
}
.typeahead-list > li {
 position: relative;
 border: none;
}
div.input.typeahead-hint,
input.typeahead-hint,
body > div.modal.cmd-palette.in > div > div > div > form > div > div.typeahead-field > span.typeahead-query > input.typeahead-hint {
 color: #546386 !important;
 background-color: transparent;
 padding: 3px 10px;
}
.typeahead-dropdown > li > a,
.typeahead-list > li > a {
 display: block;
 padding: 5px;
 clear: both;
 font-weight: 400;
 line-height: 1.7;
 border: 1px solid #202937;
 border-bottom-color: rgba(75,95,118,.55);
}
body > div.modal.cmd-palette.in > div {
 min-width: 750px;
 margin: 150px auto;
}
.typeahead-container strong {
 font-weight: bolder;
 color: #0b98c8;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
 color: #ffffff;
 background-color: #008ebf;
 border-color: #008ebf;
 border-style: solid;
 border-width: 1px;
 border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
 background-color: #dc6972;
 border-color: #dc6972;
 border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
 background-color: #48a667;
 border-color: #48a667;
 border-radius: 0px;
}
.jupyter-dashboard-menu-item.selected::before {
 font-family: 'FontAwesome' !important;
 content: '\f00c' !important;
 position: absolute !important;
 color: #0b98c8 !important;
 left: 0px !important;
 top: 13px !important;
 font-size: 12px !important;
}
.shortcut_key,
span.shortcut_key {
 display: inline-block;
 width: 16ex;
 text-align: right;
 font-family: monospace;
}
.jupyter-keybindings {
 padding: 1px;
 line-height: 24px;
 border-bottom: 1px solid rgba(75,95,118,.30);
}
.jupyter-keybindings i {
 background: #252e3a;
 font-size: small;
 padding: 5px;
 margin-left: 7px;
}
div#short-key-bindings-intro.well,
.well {
 background-color: #252b35;
 border: 1px solid #252b35;
 color: #a2b0c7;
 border-radius: 2px;
 -webkit-box-shadow: none;
 box-shadow: none;
}
#texteditor-backdrop {
 background: #1a2028;
 background-color: #1a2028;
}
#texteditor-backdrop #texteditor-container .CodeMirror-gutter,
#texteditor-backdrop #texteditor-container .CodeMirror-gutters {
 background: #334050;
 background-color: #334050;
 color: #546386;
}
.edit_app #menubar .navbar {
 margin-bottom: 0px;
}
#texteditor-backdrop #texteditor-container {
 padding: 0px;
 background-color: #293340;
 box-shadow: none;
}
.terminal-app {
 background: #1a2028;
}
.terminal-app > #header {
 background: #1a2028;
}
.terminal-app .terminal {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 color: #cdd2e9;
 background: #293340;
 padding: 0.4em;
 border-radius: 2px;
 -webkit-box-shadow: none;
 box-shadow: none;
}
.terminal .xterm-viewport {
 background-color: #293340;
 color: #cdd2e9;
 overflow-y: auto;
}
.terminal .xterm-color-0 {
 color: #0b98c8;
}
.terminal .xterm-color-1 {
 color: #e17e85;
}
.terminal .xterm-color-2 {
 color: #4cb2ff;
}
.terminal .xterm-color-3 {
 color: #e17e85;
}
.terminal .xterm-color-4 {
 color: #51c0ef;
}
.terminal .xterm-color-5 {
 color: #61ba86;
}
.terminal .xterm-color-6 {
 color: #be86e3;
}
.terminal .xterm-color-7 {
 color: #ffec8e;
}
.terminal .xterm-color-8 {
 color: #51c0ef;
}
.terminal .xterm-color-9 {
 color: #61ba86;
}
.terminal .xterm-color-10 {
 color: #e17e85;
}
.terminal .xterm-color-14 {
 color: #be86e3;
}
.terminal .xterm-bg-color-15 {
 background-color: #293340;
}
.terminal:not(.xterm-cursor-style-underline):not(.xterm-cursor-style-bar) .terminal-cursor {
 background-color: #0b98c8;
 color: #293340;
}
.terminal:not(.focus) .terminal-cursor {
 outline: 1px solid #0b98c8;
 outline-offset: -1px;
}
.celltoolbar {
 font-size: 100%;
 padding-top: 3px;
 border-color: transparent;
 border-bottom: thin solid rgba(0,156,209,.3);
 background: transparent;
}
.cell-tag,
.tags-input input,
.tags-input button {
 color: #a2b0c7;
 background-color: #1a2028;
 background-image: none;
 border: 1px solid #a2b0c7;
 border-radius: 1px;
 box-shadow: none;
 width: inherit;
 font-size: inherit;
 height: 22px;
 line-height: 22px;
}
#notebook-container > div.cell.code_cell.rendered.selected > div.input > div.inner_cell > div.ctb_hideshow.ctb_show > div > div > button,
#notebook-container > div.input > div.inner_cell > div.ctb_hideshow.ctb_show > div > div > button {
 font-size: 10pt;
 color: #a2b0c7;
 background-color: #1a2028;
 background-image: none;
 border: 1px solid #a2b0c7;
 border-radius: 1px;
 box-shadow: none;
 width: inherit;
 font-size: inherit;
 height: 22px;
 line-height: 22px;
}
div#pager #pager-contents {
 background: #1a2028 !important;
 background-color: #1a2028 !important;
}
div#pager pre {
 color: #cdd2e9 !important;
 background: #293340 !important;
 background-color: #293340 !important;
 padding: 0.4em;
}
div#pager .ui-resizable-handle {
 top: 0px;
 height: 8px;
 background: #0b98c8 !important;
 border-top: 1px solid #0b98c8;
 border-bottom: 1px solid #0b98c8;
}
div.CodeMirror,
div.CodeMirror pre {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 color: #cdd2e9;
}
div.CodeMirror-lines {
 padding-bottom: .9em;
 padding-left: .5em;
 padding-right: 1.5em;
 padding-top: .7em;
}
span.ansiblack,
.ansi-black-fg {
 color: #2b303b;
}
span.ansiblue,
.ansi-blue-fg,
.ansi-blue-intense-fg {
 color: #61afef;
}
span.ansigray,
.ansi-gray-fg,
.ansi-gray-intense-fg {
 color: #899ab8;
}
span.ansigreen,
.ansi-green-fg {
 color: #8fca9a;
}
.ansi-green-intense-fg {
 color: #899ab8;
}
span.ansipurple,
.ansi-purple-fg,
.ansi-purple-intense-fg {
 color: #b399ef;
}
span.ansicyan,
.ansi-cyan-fg,
.ansi-cyan-intense-fg {
 color: #b399ef;
}
span.ansiyellow,
.ansi-yellow-fg,
.ansi-yellow-intense-fg {
 color: #ffec8e;
}
span.ansired,
.ansi-red-fg,
.ansi-red-intense-fg {
 color: #e07a7a;
}
div.output-stderr {
 background-color: #e07a7a;
}
div.output-stderr pre {
 color: #d0d4e6;
}
div.js-error {
 color: #e07a7a;
}
.ipython_tooltip {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 border: 2px solid #252c36;
 background: #363f4e;
 background-color: #363f4e;
 border-radius: 2px;
 overflow-x: visible;
 overflow-y: visible;
 box-shadow: none;
 position: absolute;
 z-index: 1000;
}
.ipython_tooltip .tooltiptext pre {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 background: #363f4e;
 background-color: #363f4e;
 color: #cdd2e9;
 overflow-x: visible;
 overflow-y: visible;
 max-width: 900px;
}
div#tooltip.ipython_tooltip {
 overflow-x: wrap;
 overflow-y: visible;
 max-width: 800px;
}
div.tooltiptext.bigtooltip {
 overflow-x: visible;
 overflow-y: scroll;
 height: 400px;
 max-width: 800px;
}
.cm-s-ipython.CodeMirror {
 font-family: monospace, monospace;
 font-size: 11pt;
 background: #293340;
 color: #cdd2e9;
 border-radius: 2px;
 font-style: normal;
 font-weight: normal;
}
.cm-s-ipython div.CodeMirror-selected {
 background: #334050;
}
.CodeMirror-gutters {
 border: none;
 border-right: 1px solid #334050 !important;
 background-color: #334050 !important;
 background: #334050 !important;
 border-radius: 0px;
 white-space: nowrap;
}
.cm-s-ipython .CodeMirror-gutters {
 background: #334050;
 border: none;
 border-radius: 0px;
 width: 36px;
}
.cm-s-ipython .CodeMirror-linenumber {
 color: #546386;
}
.CodeMirror-sizer {
 margin-left: 40px;
}
.CodeMirror-linenumber,
div.CodeMirror-linenumber,
.CodeMirror-gutter.CodeMirror-linenumberdiv.CodeMirror-gutter.CodeMirror-linenumber {
 padding-right: 1px;
 margin-left: 0px;
 margin: 0px;
 width: 26px !important;
 padding: 0px;
 text-align: right;
}
.CodeMirror-linenumber {
 color: #546386;
}
.cm-s-ipython .CodeMirror-cursor {
 border-left: 2px solid #0095ff !important;
}
.cm-s-ipython span.cm-comment {
 color: #667fb1;
 font-style: italic;
}
.cm-s-ipython span.cm-atom {
 color: #be86e3;
}
.cm-s-ipython span.cm-number {
 color: #51c0ef;
}
.cm-s-ipython span.cm-property {
 color: #cdd2e9;
}
.cm-s-ipython span.cm-attribute {
 color: #cdd2e9;
}
.cm-s-ipython span.cm-keyword {
 color: #4cb2ff;
 font-weight: normal;
}
.cm-s-ipython span.cm-string {
 color: #61ba86;
}
.cm-s-ipython span.cm-meta {
 color: #ffec8e;
}
.cm-s-ipython span.cm-operator {
 color: #00b4ff;
}
.cm-s-ipython span.cm-builtin {
 color: #e17e85;
}
.cm-s-ipython span.cm-variable {
 color: #cdd2e9;
}
.cm-s-ipython span.cm-variable-2 {
 color: #e17e85;
}
.cm-s-ipython span.cm-variable-3 {
 color: #ffec8e;
}
.cm-s-ipython span.cm-def {
 color: #ffec8e;
 font-weight: normal;
}
.cm-s-ipython span.cm-error {
 background: rgba(191,97,106,.4);
}
.cm-s-ipython span.cm-tag {
 color: #be86e3;
}
.cm-s-ipython span.cm-link {
 color: #51c0ef;
}
.cm-s-ipython span.cm-storage {
 color: #be86e3;
}
.cm-s-ipython span.cm-entity {
 color: #be86e3;
}
.cm-s-ipython span.cm-quote {
 color: #61ba86;
}
div.CodeMirror span.CodeMirror-matchingbracket {
 color: #ffffff;
 font-weight: bold;
 background-color: #4c8be2;
}
div.CodeMirror span.CodeMirror-nonmatchingbracket {
 color: #ffffff;
 font-weight: bold;
 background: rgba(191,97,106,.4) !important;
}
.cm-header-1 {
 font-size: 215%;
}
.cm-header-2 {
 font-size: 180%;
}
.cm-header-3 {
 font-size: 150%;
}
.cm-header-4 {
 font-size: 120%;
}
.cm-header-5 {
 font-size: 100%;
}
.cm-s-default .cm-hr {
 color: #00b4ff;
}
div.cell.text_cell .cm-s-default .cm-header {
 font-family: sans-serif;
 font-weight: normal;
 color: #0b98c8 !important;
 margin-top: 0.3em !important;
 margin-bottom: 0.3em !important;
}
div.cell.text_cell .cm-s-default span.cm-variable-2 {
 color: #b0bdd7 !important;
}
div.cell.text_cell .cm-s-default span.cm-variable-3 {
 color: #ffec8e !important;
}
.cm-s-default span.cm-comment {
 color: #667fb1 !important;
}
.cm-s-default .cm-tag {
 color: #8fb36a;
}
.cm-s-default .cm-builtin {
 color: #e17e85;
}
.cm-s-default .cm-string {
 color: #61ba86;
}
.cm-s-default .cm-keyword {
 color: #4cb2ff;
}
.cm-s-default .cm-number {
 color: #51c0ef;
}
.cm-s-default .cm-error {
 color: #be86e3;
}
.cm-s-default .cm-link {
 color: #51c0ef;
}
.cm-s-default .cm-atom {
 color: #51c0ef;
}
.cm-s-default .cm-def {
 color: #ffec8e;
}
.CodeMirror-cursor {
 border-left: 2px solid #0095ff !important;
 border-right: none;
 width: 0;
}
.cm-s-default div.CodeMirror-selected {
 background: #334050;
}
.cm-s-default .cm-selected {
 background: #334050;
}
.MathJax_Display,
.MathJax {
 border: 0 !important;
 font-size: 100% !important;
 text-align: center !important;
 margin: 0em !important;
 line-height: 2.25 !important;
}
.MathJax:focus,
body :focus .MathJax {
 display: inline-block !important;
}
.MathJax:focus,
body :focus .MathJax {
 display: inline-block !important;
}
.completions {
 position: absolute;
 z-index: 110;
 overflow: hidden;
 border: medium solid rgba(0,156,209,.5);
 box-shadow: none;
 line-height: 1;
}
.completions select {
 background: #293340;
 background-color: #293340;
 outline: none;
 border: none;
 padding: 0px;
 margin: 0px;
 margin-left: 2px;
 overflow: auto;
 font-family: monospace, monospace;
 font-size: 11pt;
 color: #cdd2e9;
 width: auto;
}
div#maintoolbar {
 display: none !important;
}
#header-container {
 display: none !important;
}

<script>
    MathJax.Hub.Config({
        "HTML-CSS": {
            /*preferredFont: "TeX",*/
            /*availableFonts: ["TeX", "STIX"],*/
            styles: {
                scale: 100,
                ".MathJax_Display": {
                    "font-size": "100%",
                }
            }
        }
    });
</script>
     </style>



```

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

SparkSession: SparkSession is a combination of all these differents contexts.

spark = SparkSession \
    .builder \
    .appName('Python Spark create RDD example') \
    .config('spark.some.config.option', 'some-value') \
    .getOrCreate()

spark = SparkSession.builder.appName('Python Spark create RDD example').config('spark.some.config.option', 'some-value').getOrCreate()

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

df = spark.sparkContext.parallelize([(1,2,3, 'a b c'),
                                    (4,5,6, 'd e f'),
                                    (7,8,9, 'g h i')])

Why we use parallelize in Spark?
parallelize() method is the SparkContext's parallelize method to create a parallelized collection. This allows Spark to distribute the data across multiple nodes, instead of depending on a single node to process the data: Now that we have created ... Get PySpark Cookbook now with O'Reilly online learning.

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

# SparkSession: SparkSession is a combination of all these differents contexts.

# conf = SparkConf().setMaster("local").setAppName("My App")
# sc = SparkContext(conf = conf)
# lines = sc.textFile('README.md')
# lines
# pythonLines = lines.filter(lambda line: "Python" in line)
# pythonLines

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```


```python
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()
spark
```





    <div>
        <p><b>SparkSession - in-memory</b></p>

<div>
    <p><b>SparkContext</b></p>

    <p><a href="http://9a16fcc4671d:4040">Spark UI</a></p>

    <dl>
      <dt>Version</dt>
        <dd><code>v3.2.0</code></dd>
      <dt>Master</dt>
        <dd><code>local[*]</code></dd>
      <dt>AppName</dt>
        <dd><code>Name_Spark</code></dd>
    </dl>
</div>

    </div>




```
                    
                    ##### Creating Method #####

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

                    ##### createDataFrame method #####

df = spark.createDataFrame()
- We got total control over the schema customization

from pyspark.sql.types import StructType,StructField, StringType, IntegerType

data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])
 
df = spark.createDataFrame(data=data2,schema=schema)
df.printSchema()
df.show(truncate=False)

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

                    ###### parallerize #####
                    
- We do not have the total control over/about schema

columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

df_rdd = spark.sparkContext.parallelize(data)
- If you to print you gonna to receive "RDD STRUCTURE"

df = spark.createDataFrame(df_rdd).toDF(*columns)

OR

df = spark.sparkContext.parallelize(data).toDF(*columns)

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```

```
        
            ##### Function #####

- df.toPandas()
- df.show()
- df.toDF()

```


```python
# appl_stock.csv 
# people.json

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.json('people.json')
df.show()
```

    +----+-------+------+
    | age|   name|weight|
    +----+-------+------+
    |null|Michael|    80|
    |  30|   Andy|    86|
    |  19| Justin|    67|
    |null|    jun|    99|
    |  22|  Carls|    77|
    |  31| Jordan|    83|
    +----+-------+------+
    


```

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

new_names = [new_columns.get(col,col) for col in df.columns]
df.toDF(*new_names).show(4)

new_columns = {'age':'AGE', 'name':'NAME'}
new_names = [new_columns.get(col,col) for col in df.columns]
df.toDF(*new_names).show(4)

+----+-------+------+
| AGE|   NAME|weight|
+----+-------+------+
|null|Michael|    80|
|  30|   Andy|    86|
|  19| Justin|    67|
|null|    jun|    99|
+----+-------+------+
only showing top 4 row



-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```


```python
new_columns = {'age':'AGE', 'name':'NAME'}
```


```python
new_columns = {'age':'AGE', 'name':'NAME'}
new_names = [new_columns.get(col,col) for col in df.columns]
df.toDF(*new_names).show(4)
```

    +----+-------+------+
    | AGE|   NAME|weight|
    +----+-------+------+
    |null|Michael|    80|
    |  30|   Andy|    86|
    |  19| Justin|    67|
    |null|    jun|    99|
    +----+-------+------+
    only showing top 4 rows
    



```python
new_columns = {'age':'AGE', 'name':'NAME'}

list = []
for col in df.columns:
    list.append(new_columns.get(col,col))

df.toDF(*list).show(4)
```

    +----+-------+------+
    | AGE|   NAME|weight|
    +----+-------+------+
    |null|Michael|    80|
    |  30|   Andy|    86|
    |  19| Justin|    67|
    |null|    jun|    99|
    +----+-------+------+
    only showing top 4 rows
    



```python
new_columns = {'age':'AGE', 'name':'NAME'}

list = []
for col in df.columns:
    list.append(new_columns.get(col,col))

list
```




    ['AGE', 'NAME', 'weight']




```python

```


```python
df.collect()
```




    [Row(col1=1, col2=2, col3=3, col4='a b c'),
     Row(col1=4, col2=5, col3=6, col4='d e f'),
     Row(col1=7, col2=8, col3=9, col4='g h i')]




```python
#SQLContext.getConf(spark.driver.maxResultSize)
```

<ul>
  <li><b> df.printSchema() </b></li>
      <dd></dd>
          <p>
        
  <li><b> df.describe()  </b></li>
      <dd></dd>
          <p>      
        
  <li><b>df.select(*expression(.show()</b></li>
      <dd></dd>
          <p>
              
  <li><b>df.show(), df.head(), df,tail()</b></li>
      <dd></dd>
          <p>
              
  <li><b>df.columns #['Name', 'Age]</b></li>
      <dd></dd>
          <p>
              
  <li><b> df.select('column_name') </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.select(['column_name',]) </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.select['column_name'] </b></li>
  <dd> - ['Name', 'Age ]</dd>
      <p>      
          
  <li><b> df.describe() </b></li>
          <dd> </dd>
    <p>
        
  <li><b> df.types() </b></li>
          <dd> - (['Name', 'string'])</dd>
    <p>
        
  <li><b> spark = SparkSession.builder.appName('Name_Spark').getOrCreate() </b></li>
      <dd></dd>
          <p>      
        
  <li><b> df = spark.read.csv (-File.csv-) </b></li>
      <dd></dd>
          <p>  
              
  <li><b> expression = [func.lower(func.col(x).alias(x) for x in df.columns] </b></li>
      <dd></dd>
          <p> 

</ul>
 

<dl>
   <dt><b> </b></dt>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd>  </dd>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd> </dd>
</dl>


```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv('test1.csv') #  header=True, inferSchema = True)

df.show()
type(df)
```

    +---------+---+----------+------+
    |      _c0|_c1|       _c2|   _c3|
    +---------+---+----------+------+
    |     Name|age|Experience|Salary|
    |    Krish| 31|        10| 30000|
    |Sudhanshu| 30|         8| 25000|
    |    Sunny| 29|         4| 20000|
    |     Paul| 24|         3| 20000|
    |   Harsha| 21|         1| 15000|
    |  Shubham| 23|         2| 18000|
    +---------+---+----------+------+
    





    pyspark.sql.dataframe.DataFrame




```python

```


```python

```


```python

```


```python

```


```python
my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
#dp = pd.DataFrame(my_list,columns=['A', 'B', 'C']) <----- to Pandas
ds = spark.createDataFrame(my_list, ['A', 'B', 'C'])
ds
```




    DataFrame[A: string, B: bigint, C: bigint]




```python
ds.toPandas()
```

                                                                                    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



# Importing and creating spark data frame


```python
df = spark.sparkContext.parallelize([(1, 2, 3, 'a b c'),
(4, 5, 6, 'd e f'),
(7, 8, 9, 'g h i')]).toDF(['col1', 'col2', 'col3','col4'])

```


```python
my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
#dp = pd.DataFrame(my_list,columns=['A', 'B', 'C']) <----- to Pandas
ds = spark.createDataFrame(my_list, ['A', 'B', 'C'])
ds.show()

# or

ds_v0 = spark.createDataFrame([(1, 2, 3, 'a b c'),
                             (4, 5, 6, 'd e f'),
                             (7, 8, 9, 'g h i')],['col1', 'col2', 'col3','col4'])

ds_v0.show()                        
```

    +---+---+----+
    |  A|  B|   C|
    +---+---+----+
    |  a|  1|null|
    |  b|  2|   3|
    |  c|  3|   4|
    +---+---+----+
    
    +----+----+----+-----+
    |col1|col2|col3| col4|
    +----+----+----+-----+
    |   1|   2|   3|a b c|
    |   4|   5|   6|d e f|
    |   7|   8|   9|g h i|
    +----+----+----+-----+
    



```python
# df = spark.read.csv('infojobs_dataset.csv', sep ='<anything>'header = True, inferSchema = True)
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.toPandas()
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207595</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207596</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207599</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>



# columns( ), .describe( ), .select( )


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
display(df.toPandas())

df.describe().toPandas()
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207595</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207596</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207599</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>summary</th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>count</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>mean</td>
      <td>5.5</td>
      <td>None</td>
      <td>None</td>
      <td>7207364.9</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stddev</td>
      <td>3.0276503540974917</td>
      <td>None</td>
      <td>None</td>
      <td>504.23615499083047</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>min</td>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7206056</td>
      <td>Atendente De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>max</td>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    ['id',
     'site',
     'url',
     'codigo',
     'profissao',
     'salario',
     'localidade',
     'conteudo',
     'empresa',
     'data do scraping',
     '1_dif_data']



# drop( ), df.withColumnRenamed('_c0','sno')


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
display(df.toPandas())

print('multi drop columns')
""" The * needs to come outside of the brackets if there are multiple columns to drop """

df_drop = df.drop(*['url', 'codigo', 'salario'])
df_drop.toPandas()
display(df_drop.toPandas())


print('Renaming')

df_renamed = df.withColumnRenamed('id', 'ID_NUMBER')
display(df_renamed.toPandas().head(3))
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207595</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207596</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207599</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>


    multi drop columns



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>profissao</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>Atendente De Vendas</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>Atendimento - Bh</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>Consultor De Vendas</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>Instrutor(A) De Solda</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>


    Renaming



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID_NUMBER</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>


# adding columns: .lit(values), .otherwise(), when(), &


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.toPandas().head(3)


from pyspark.sql.functions import when,col,lit


df_with_column_lit = df.withColumn('lit_column', lit(1000)) 
display(df_with_column_lit.toPandas().head(3))


df_alias = df.withColumn('alias_column', lit('alias_values'))
df_alias.toPandas().head(3)

#df_v1.withColumn('new_column_Age',df_v1['age']*2)
# df3 = df.select(col("EmpId"),col("Salary"),lit("1").alias("lit_value1"))
# df3 = df.select(col("EmpId"),col("Salary"),lit("1").alias("lit_value1"))
# df3 = df2.withColumn("lit_value2", when(col("Salary") >=40000 & col("Salary") <= 50000,lit("100")).otherwise(lit("200")))
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
      <th>lit_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>1000</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
      <th>alias_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>alias_values</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>alias_values</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>alias_values</td>
    </tr>
  </tbody>
</table>
</div>



# types values, casting column type, type(), .dtypes
### https://sparkbyexamples.com/pyspark/pyspark-cast-column-type/


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()
df.toPandas().head(3)

display(type(df))

display(df.dtypes)

from pyspark.sql.types import IntegerType,BooleanType,DateType

#########################################################################################

df_cast = df.withColumn("codigo", df.codigo.cast(IntegerType()))
display(df_cast)
df_cast.printSchema()

#########################################################################################

df_sql = df.createOrReplaceTempView('Cast_SQL')
df_sql =  spark.sql("SELECT STRING(profissao), INT(codigo), INT(salario) from Cast_SQL")
df_sql.printSchema()

#########################################################################################

# Convert String to Integer Type
#df.withColumn("age",df.age.cast(IntegerType()))
#df.withColumn("age",df.age.cast('int'))
#df.withColumn("age",df.age.cast('integer'))

# Using select
#df.select(col("age").cast('int').alias("age"))

#Using selectExpr()
#df.selectExpr("cast(age as int) age")

#Using with spark.sql()
#spark.sql("SELECT INT(age),BOOLEAN(isGraduated),DATE(jobStartDate) from CastExample")
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    



    pyspark.sql.dataframe.DataFrame



    [('id', 'string'),
     ('site', 'string'),
     ('url', 'string'),
     ('codigo', 'string'),
     ('profissao', 'string'),
     ('salario', 'string'),
     ('localidade', 'string'),
     ('conteudo', 'string'),
     ('empresa', 'string'),
     ('data do scraping', 'string'),
     ('1_dif_data', 'string')]



    DataFrame[id: string, site: string, url: string, codigo: int, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: integer (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    
    root
     |-- profissao: string (nullable = true)
     |-- codigo: integer (nullable = true)
     |-- salario: integer (nullable = true)
    


# conditions, .union( ) SQL


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()
df.toPandas().head(3)
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
# SQl
df.createOrReplaceTempView('name_created')

results = spark.sql('SELECT * FROM name_created')
results.toPandas().head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.createOrReplaceTempView('name_created')

results_sql = spark.sql('select * from name_created where codigo < 7207593')
results_sql.toPandas()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()

df_1 = df.head(1)
df_2 = df.tail(1)


df_11 = spark.createDataFrame(df_1)
df_22 = spark.createDataFrame(df_2)

df_concat = df_11.union(df_22)
display(df_concat)
df_concat.toPandas()
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    



    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>



# upper( ), lower( ) case


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()



for col in df.columns:
    df = df.withColumnRenamed(col, col.upper())
df.show()


#df = df.toDF(*[c.lower() for c in df.columns])
#df.show()

```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    | ID|    SITE|                 URL| CODIGO|           PROFISSAO|             SALARIO|         LOCALIDADE|            CONTEUDO|             EMPRESA|DATA DO SCRAPING|1_DIF_DATA|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    |  1|infojobs|https://www.infoj...|7207593| Atendente De Vendas| 1.500,00 a  1.80...|      Sao Paulo, SP|Area e especializ...|            CESARMAQ|      2021-04-29|   21 days|
    |  2|infojobs|https://www.infoj...|7207597| Vue.Js Tech Lead...|          A combinar|      Fortaleza, CE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  3|infojobs|https://www.infoj...|7206929|    Atendimento - Bh|           1.135,00 | Belo Horizonte, MG|Area e especializ...|   VALLOR BENEFICIOS|      2021-04-29|   21 days|
    |  4|infojobs|https://www.infoj...|7207595| Vue.Js Tech Lead...|          A combinar|         Recife, PE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  5|infojobs|https://www.infoj...|7206056| Consultor De Vendas| 1.000,00 a  3.00...|        Caruaru, PE|Area e especializ...|Dragorayeb Incorp...|      2021-04-29|   21 days|
    |  6|infojobs|https://www.infoj...|7207596| Vue.Js Tech Lead...|          A combinar|       Curitiba, PR|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  7|infojobs|https://www.infoj...|7207541| Instrutor(A) De ...|          A combinar|       Curitiba, PR|Area e especializ...|     CEBRAC CURITIBA|      2021-04-29|   21 days|
    |  8|infojobs|https://www.infoj...|7207599| Vue.Js Tech Lead...|          A combinar|      Guarulhos, SP|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  9|infojobs|https://www.infoj...|7207543| Auxiliar De Manu...| 1.500,00 a  1.60...|       Campinas, SP|Area e especializ...|HM CONSULTORIA E ...|      2021-04-29|   21 days|
    | 10|infojobs|https://www.infoj...|7207600| Vue.Js Tech Lead...|          A combinar|       Brasilia, DF|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    



```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()

import pyspark.sql.functions as f

#Customer_Data = Customer_Data.withColumn("Email_Updated",func.lower(func.col("Email")))

for colun in df.columns:
    df = df.withColumn(colun,f.lower(f.col(colun)))
df.show()


#import pandas as pd
#df = df.toDF(*[df.withColumn(colun, lower(colun)) for colun in df.columns])
#df.show()

#new_df = df.withColumn('Channel', lower(df.Channel))
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    | id|    site|                 url| codigo|           profissao|             salario|         localidade|            conteudo|             empresa|data do scraping|1_dif_data|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    |  1|infojobs|https://www.infoj...|7207593| atendente de vendas| 1.500,00 a  1.80...|      sao paulo, sp|area e especializ...|            cesarmaq|      2021-04-29|   21 days|
    |  2|infojobs|https://www.infoj...|7207597| vue.js tech lead...|          a combinar|      fortaleza, ce|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  3|infojobs|https://www.infoj...|7206929|    atendimento - bh|           1.135,00 | belo horizonte, mg|area e especializ...|   vallor beneficios|      2021-04-29|   21 days|
    |  4|infojobs|https://www.infoj...|7207595| vue.js tech lead...|          a combinar|         recife, pe|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  5|infojobs|https://www.infoj...|7206056| consultor de vendas| 1.000,00 a  3.00...|        caruaru, pe|area e especializ...|dragorayeb incorp...|      2021-04-29|   21 days|
    |  6|infojobs|https://www.infoj...|7207596| vue.js tech lead...|          a combinar|       curitiba, pr|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  7|infojobs|https://www.infoj...|7207541| instrutor(a) de ...|          a combinar|       curitiba, pr|area e especializ...|     cebrac curitiba|      2021-04-29|   21 days|
    |  8|infojobs|https://www.infoj...|7207599| vue.js tech lead...|          a combinar|      guarulhos, sp|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  9|infojobs|https://www.infoj...|7207543| auxiliar de manu...| 1.500,00 a  1.60...|       campinas, sp|area e especializ...|hm consultoria e ...|      2021-04-29|   21 days|
    | 10|infojobs|https://www.infoj...|7207600| vue.js tech lead...|          a combinar|       brasilia, df|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    



```python
import pyspark.sql.functions as f


for colun in df.columns:
    df = df.withColumn(colun,f.lower(f.col(colun)))
df.show()
```


```python
Customer_Data = Customer_Data.withColumn("Email_Updated",func.lower(func.col("Email")))
```

# Apply( ) with multi columns


```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()

df = df.toPandas().head(3)
df
```

    WARNING: An illegal reflective access operation has occurred
    WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/usr/local/spark-3.2.0-bin-hadoop3.2/jars/spark-unsafe_2.12-3.2.0.jar) to constructor java.nio.DirectByteBuffer(long,int)
    WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
    WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
    WARNING: All illegal access operations will be denied in a future release
    Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    21/11/16 19:53:41 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    21/11/16 19:53:42 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.



    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
!pip install unidecode
from unidecode import unidecode

for col in df.columns:
    df[col] = df[col].apply(unidecode)
df
```

    Requirement already satisfied: unidecode in /opt/conda/lib/python3.9/site-packages (1.3.2)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
from jupyterthemes import get_themes
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    /tmp/ipykernel_50/3930510084.py in <module>
    ----> 1 from jupyterthemes import get_themes
    

    ModuleNotFoundError: No module named 'jupyterthemes'



```python
!pip install jupyterthemes
import jupyterthemes as jt
#from jupyterthemes.stylefx import set_nb_theme
#set_nb_theme('chesterish')
#!pip list
!jt -t chesterish -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T

```

    Collecting jupyterthemes
      Downloading jupyterthemes-0.20.0-py2.py3-none-any.whl (7.0 MB)
         |████████████████████████████████| 7.0 MB 1.0 MB/s            
    [?25hRequirement already satisfied: matplotlib>=1.4.3 in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (3.4.3)
    Requirement already satisfied: ipython>=5.4.1 in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (7.29.0)
    Requirement already satisfied: notebook>=5.6.0 in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (6.4.5)
    Requirement already satisfied: jupyter-core in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (4.9.1)
    Collecting lesscpy>=0.11.2
      Downloading lesscpy-0.15.0-py2.py3-none-any.whl (46 kB)
         |████████████████████████████████| 46 kB 454 kB/s            
    [?25hRequirement already satisfied: pygments in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (2.10.0)
    Requirement already satisfied: traitlets>=4.2 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (5.1.1)
    Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (4.8.0)
    Requirement already satisfied: decorator in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (5.1.0)
    Requirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.1.3)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (3.0.21)
    Requirement already satisfied: setuptools>=18.5 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (58.5.2)
    Requirement already satisfied: backcall in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.2.0)
    Requirement already satisfied: pickleshare in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.7.5)
    Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.18.0)
    Collecting ply
      Downloading ply-3.11-py2.py3-none-any.whl (49 kB)
         |████████████████████████████████| 49 kB 372 kB/s            
    [?25hRequirement already satisfied: six in /opt/conda/lib/python3.9/site-packages (from lesscpy>=0.11.2->jupyterthemes) (1.16.0)
    Requirement already satisfied: pyparsing>=2.2.1 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (2.4.7)
    Requirement already satisfied: numpy>=1.16 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (1.20.3)
    Requirement already satisfied: python-dateutil>=2.7 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (2.8.2)
    Requirement already satisfied: pillow>=6.2.0 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (8.3.2)
    Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (0.11.0)
    Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (1.3.2)
    Requirement already satisfied: tornado>=6.1 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (6.1)
    Requirement already satisfied: jupyter-client>=5.3.4 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (7.0.6)
    Requirement already satisfied: jinja2 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (3.0.2)
    Requirement already satisfied: terminado>=0.8.3 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (0.12.1)
    Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (0.2.0)
    Requirement already satisfied: Send2Trash>=1.5.0 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (1.8.0)
    Requirement already satisfied: prometheus-client in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (0.12.0)
    Requirement already satisfied: pyzmq>=17 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (22.3.0)
    Requirement already satisfied: argon2-cffi in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (21.1.0)
    Requirement already satisfied: nbformat in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (5.1.3)
    Requirement already satisfied: ipykernel in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (6.4.2)
    Requirement already satisfied: nbconvert in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (6.2.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/lib/python3.9/site-packages (from jedi>=0.16->ipython>=5.4.1->jupyterthemes) (0.8.2)
    Requirement already satisfied: nest-asyncio>=1.5 in /opt/conda/lib/python3.9/site-packages (from jupyter-client>=5.3.4->notebook>=5.6.0->jupyterthemes) (1.5.1)
    Requirement already satisfied: entrypoints in /opt/conda/lib/python3.9/site-packages (from jupyter-client>=5.3.4->notebook>=5.6.0->jupyterthemes) (0.3)
    Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.9/site-packages (from pexpect>4.3->ipython>=5.4.1->jupyterthemes) (0.7.0)
    Requirement already satisfied: wcwidth in /opt/conda/lib/python3.9/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.4.1->jupyterthemes) (0.2.5)
    Requirement already satisfied: cffi>=1.0.0 in /opt/conda/lib/python3.9/site-packages (from argon2-cffi->notebook>=5.6.0->jupyterthemes) (1.14.6)
    Requirement already satisfied: debugpy<2.0,>=1.0.0 in /opt/conda/lib/python3.9/site-packages (from ipykernel->notebook>=5.6.0->jupyterthemes) (1.4.1)
    Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.9/site-packages (from jinja2->notebook>=5.6.0->jupyterthemes) (2.0.1)
    Requirement already satisfied: testpath in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.0)
    Requirement already satisfied: mistune<2,>=0.8.1 in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.8.4)
    Requirement already satisfied: jupyterlab-pygments in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.1.2)
    Requirement already satisfied: pandocfilters>=1.4.1 in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (1.5.0)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.4)
    Requirement already satisfied: defusedxml in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.7.1)
    Requirement already satisfied: bleach in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (4.1.0)
    Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /opt/conda/lib/python3.9/site-packages (from nbformat->notebook>=5.6.0->jupyterthemes) (4.1.2)
    Requirement already satisfied: pycparser in /opt/conda/lib/python3.9/site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=5.6.0->jupyterthemes) (2.20)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /opt/conda/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat->notebook>=5.6.0->jupyterthemes) (0.17.3)
    Requirement already satisfied: attrs>=17.4.0 in /opt/conda/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat->notebook>=5.6.0->jupyterthemes) (21.2.0)
    Requirement already satisfied: packaging in /opt/conda/lib/python3.9/site-packages (from bleach->nbconvert->notebook>=5.6.0->jupyterthemes) (21.2)
    Requirement already satisfied: webencodings in /opt/conda/lib/python3.9/site-packages (from bleach->nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.1)
    Installing collected packages: ply, lesscpy, jupyterthemes
    Successfully installed jupyterthemes-0.20.0 lesscpy-0.15.0 ply-3.11



```python

```


```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
df.printSchema()
```

    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    



```python
display(df)
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



```python
df.show(5)
```

    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    | id|    site|                 url| codigo|           profissao|             salario|         localidade|            conteudo|             empresa|data do scraping|1_dif_data|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    |  1|infojobs|https://www.infoj...|7207593| Atendente De Vendas| 1.500,00 a  1.80...|      Sao Paulo, SP|Area e especializ...|            CESARMAQ|      2021-04-29|   21 days|
    |  2|infojobs|https://www.infoj...|7207597| Vue.Js Tech Lead...|          A combinar|      Fortaleza, CE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  3|infojobs|https://www.infoj...|7206929|    Atendimento - Bh|           1.135,00 | Belo Horizonte, MG|Area e especializ...|   VALLOR BENEFICIOS|      2021-04-29|   21 days|
    |  4|infojobs|https://www.infoj...|7207595| Vue.Js Tech Lead...|          A combinar|         Recife, PE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  5|infojobs|https://www.infoj...|7206056| Consultor De Vendas| 1.000,00 a  3.00...|        Caruaru, PE|Area e especializ...|Dragorayeb Incorp...|      2021-04-29|   21 days|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    only showing top 5 rows
    



```python
import csv

df = csv.loads(re.sub(72, 'setenta e dois'))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    /tmp/ipykernel_33/2506699769.py in <module>
          1 import csv
          2 
    ----> 3 df = csv.loads(re.sub(72, 'setenta e dois'))
    

    AttributeError: module 'csv' has no attribute 'loads'



```python
##################################################################################################
```

<ul>
  <li> df_1.union(df_2) </li>
  <li> expression = [func.lower(func.col(x).alias(x) for x in df.columns]</li>
  <li> df.select(*expression(.show() </li>
</ul>


```python
from pyspark.sql import functions as psf

df_concat = df_11.union(df_22)
expression = [ psf.lower(psf.col(x)).alias(x) for x in df_concat.columns ]
df_concat.select(*expression).show()
```


```python
df_accents_0 = [ unidecode(x) for x in df_accents.columns]
```


```python
for item in df.head(1)[0]:
    print(item)
for item in df.head(1)[0]:
    print(item)
Krish
31
10
30000
```

<ul>
  <li><b> df.withColumn('Column_Name', df[''Column_Name']+2) </b></li>
      <dd> - DataFrame[Name: string, age: int, Experience: int, Salary: int, Experience after 2 years: int]</dd>
          <p>
        
  <li><b> df.drop('Column_Name') </b></li>
      <dd></dd>
          <p>      
        
  <li><b> df = df.withColumnRenamed('Column_Name_1',''Column_Name_2')</b></li>
      <dd> - DataFrame[New Name: string, age: int, Experience: int, Salary: int]</dd>
          <p>
              
  <li><b> sfhit+tab+tab </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.na.drop(how='all').show() </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.na.drop(how='any',thresh=2).show() </b></li>
      <dd></dd>
          <p>  
              
  <li><b> df.na.drop(how='any',subset=['Column_Name']).show() </b></li>
      <dd></dd>
          <p>

  <li style="font-size:25px;"><b> ### Filling the missing value ### </b></li>
  <li><b> df.na.fill('Missing Value').show() </b></li>            
  <li><b> df.na.fill(value=3,subset=['Experience']).show() </b></li>                       
  <li><b> df.fillna('Missing Value').show() </b></li>
  <li><b> df.fillna('Missing Value',subset=['age']).show() </b></li>
  <li><b> df.na.fill({'age':'Missing'}).show() </b></li>
              
              
  <dd> </dd>
      <p>      
            
  <li><b> df.na.fill('Missing Value').show() </b></li>
  <li><b> df.na.fill('Missing Value','Experience').show() </b></li>
  <dd> </dd>
      <p>          
          
          
  <li><b> df.describe() </b></li>
          <dd> </dd>
    <p>
        
  <li><b> df.types() </b></li>
          <dd> - (['Name', 'string'])</dd>
    <p>
        
  <li><b> spark = SparkSession.builder.appName('Name_Spark').getOrCreate() </b></li>
      <dd></dd>
          <p>      
        
  <li><b> df = spark.read.csv (-File.csv-) </b></li>
      <dd></dd>
          <p>  
              
  <li><b> expression = [func.lower(func.col(x).alias(x) for x in df.columns] </b></li>
      <dd></dd>
          <p> 

</ul>


```python
spark = SparkSession \
    .builder \
    .appName('Python Spark create RDD example') \
    .config('spark.some.config.option', 'some-value') \
    .getOrCreate()
    
df = spark.sparkContext.parallelize([(1,2,3, 23),
                                    (4,5,6, 32),
                                    (7,8,9, 52)]).toDF(['col1', 'col2', 'col3', 'col4'])
df.show()


df['new_column_created'] = df.apply()
```

    +----+----+----+----+
    |col1|col2|col3|col4|
    +----+----+----+----+
    |   1|   2|   3|  23|
    |   4|   5|   6|  32|
    |   7|   8|   9|  52|
    +----+----+----+----+
    



```python
from pyspark.ml.feature import Imputer
```


```python
imputer = Imputer(
    inputCols = ['col1','col2', 'col3', 'col4'],
outputCols = ["{}_imputed".format(c) for c in ['col1','col2', 'col3', 'col4']]
).setStrategy("mean")
```


```python
imputer.fit(df).transform(df).show()
```

    +----+----+----+----+------------+------------+------------+------------+
    |col1|col2|col3|col4|col1_imputed|col2_imputed|col3_imputed|col4_imputed|
    +----+----+----+----+------------+------------+------------+------------+
    |   1|   2|   3|  23|           1|           2|           3|          23|
    |   4|   5|   6|  32|           4|           5|           6|          32|
    |   7|   8|   9|  52|           7|           8|           9|          52|
    +----+----+----+----+------------+------------+------------+------------+
    



```python
spark_frame_for_training_mapping.toDF(*new_names).show(4)
```

# <h1 style="border:2px solid black; background-color:#33FFF4; color:red"> Filter </h1>

```

- df[(df.column > 2)].show()

- df[(df['column_name > 2')].show()

- df[(df.column_1 > 2) & (df.column_2 == 2) ].show()

- df.filter('salary <= 2000').show()

- df.spark.filter('Salary <= 20000').select(['Name', 'age']).show()

- df.filter(df_pyspark['Salary'] <=20000).show()

- df.filter((df_pyspark['Salary']<=20000) | (df['Salary']>=15000)).show()

- df.filter(~(df_pyspark['Salary']<=20000)).show()

- df_pyspark.filter(~(df_pyspark['Salary']<=20000)).show()

- df_pyspark.filter("age < 50").select('Name').show()

- df_pyspark.filter(df_pyspark["age"] < 50).select('Name').show()

- df_pyspark.filter(df_pyspark["age"] < 50).show()

- df_pyspark.filter( (df_pyspark['age'] < 30) & ~(df_pyspark['Experience'] > 30000) ).show()

- # df_pyspark_DATAFRAME.FILTERING( ( ONLY VALUES FROM df_pyspark < 30)) and (ONLY VALUES DOESNT  df_pyspark > 30000)).show()

- df_pyspark.filter(df_pyspark["age"] == 30).collect()

- result = df_pyspark.filter(df_pyspark["age"] == 30).collect()

- row = result[0]

- row.asDict()
{'Name': 'Sudhanshu', 'age': 30, 'Experience': 8, 'Salary': 25000}

- result[0].asDict()
{'Name': 'Sudhanshu', 'age': 30, 'Experience': 8, 'Salary': 25000}

- row.asDict()['Name']
'Sudhanshu'


- df.filter('Close < 500').select(['Open','Close']).show()

- df.filter("Close < 500").select('Open').show()

- df.filter(df['Close'] < 500).select('Volume').show()

- df.filter("Close < 500").select(["Open","Close"]).show()

- df.filter( (df['Close'] < 200) & (df['Open'] > 200) ).show()

- and === &

df.filter( (df['Close'] < 200) & ~(df['Open'] > 200) ).show()

# ~ NOT

=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x

### Pyspark Group And Aggregate Functions ###

- df_spark.groupBy('Name').sum()
DataFrame[Name: string, sum(salary): bigint]

- df_spark.groupBy('Name').sum().show()

- df_spark.groupBy('Departments').sum().show()

- df_spark.groupBy('Departments').mean().show()

- df_spark.groupBy('Departments').count().show()

- df_spark.agg({'Salary':'sum'}).show()

=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x

- df.head(3)

- df.head(3)[0]

- df.dtypes

- df.columns

- df_imputer.filter(df_imputer['Qual a sua escola?'].isNotNull()).toPandas().head(5)
# isNotNull())

- Dict_Null = {col:df_imputer.filter(df_imputer[col].isNull()).count() for col in df_imputer.columns}
Dict_Null
#Dict_Null = [col:df_imputer.filter(df_imputer[col].isNull()).count() for col in df_imputer.columns]                   ^
#SyntaxError: invalid syntax

- col:df_imputer.filter(df_imputer[col].isNull()).count() 

- df_imputer.filter(df_imputer['Qual o seu nome?'].isNull()).count()

- spark_frame_for_training.na.replace(['1'],['na.replace()']).show()
- spark_frame_for_training.na.replace(['1'],['na.replace()-Id'],subset=['Id']).show()

- spark_frame_for_training_ds.toDF('a','b','c','d').show()

- spark_frame_for_training_dp.columns = ['a','b','c','d']
spark_frame_for_training_dp

```

```
from pyspark.sql import SparkSession

from pyspark.sql.session import SparkSession

# from pyspark.sql.types import (StructField, StringType, IntegerType, StructType)
from pyspark.sql.types import (ArrayType, StructField, StructType, StringType, IntegerType)

spark = SparkSession.builder.getOrCreate()
spark = SparkSession.builder.appName('ops').getOrCreate()

data_schema = [StructField('age', IntegerType(), True),
              StructField('name', StringType(), True)]

final_struc = StructType(fields=data_schema)

df_v1 = spark.read.json('people.json', schema=final_struc)

df_v1.printSchema()

```

```
##### PySpark Session #####

# File location and type
# file_location = "/FileStore/tables/empresa_est.csv"
file_location = "/gov/usr_upload/source/dados.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

df

spark = SparkSession \
    .builder \
    .appName('Python Spark create RDD example') \
    .config('spark.some.config.option', 'some-value') \
    .getOrCreate()

------------------><------------------><------------------><------------------><------------------><
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark create RDD example").config("spark.some.config.option", "some-value").getOrCreate()

my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
spark.createDataFrame('my_list', ['A', 'B', 'C']

Employee = spark.createDataFrame([ ('1', 'Joe', '70000', '1'),
                                  ('2', 'Henry', '80000', '2'),
                                  ('3', 'Sam', '60000', '2'),
                                  ('4', 'Max', '90000', '1')],
                                 ['Id', 'Name', 'Sallary','DepartmentId'] )
                                 


```
##### SQL #####

df.createOrReplaceTempView('Name')

results = spark.sql("SELECT * FROM people")

results = spark.sql("select * from people WHEre age=30")

results.show()

=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x


```
##### SQL #####

df.createOrReplaceTempView('Name')

results = spark.sql("SELECT * FROM people")

results = spark.sql("select * from people WHEre age=30")

results.show()

x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x===

###### spark_dataframe to dataframe #####

df = spark.createDataFrame(data)
df
type(df)
pyspark.sql.dataframe.DataFrame

x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x===

Python Dictionary get() Method
dictionary.get(keyname, value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("brand","NEW_BRAND")
print(x)
Ford

x = car.get("price","NEW_BRAND")
print(x)
NEW_BRAND

x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x===

```

