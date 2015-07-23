Google Analytics App
====================

This is an example app which implements Google Analytics in Cantemo Portal.

Installation
------------

To install this plugin, just place the entire directory under
/opt/cantemo/portal/portal/plugins in your portal installation and then run

```
  python manage.py syncdb
```

to install all the models followed by

```
  supervisorctl restart all
```

to restart all

What's in the app
-----------------

The app consists of three different plugins, all defined in plugins.py.

* AnalyticsPluginURL 

This plugin implements IPluginURL and adds an additional url to the system for configuring the analytics plugin.
The settings page allows the user to configure which Analytics profile id to use.

* AnalyticsPluginBlock

This plugin adds the actual google analytics tracking code to every
page. This is done by inserting it into the plugin block header_css_js
which is a part of the header of every page.

* AnalyticsNavigationAdminPlugin

This plugin adds a link to the settings page to the admin menu. This
is done by adding the menu option to the plugin block
NavigationAdminPlugin.


