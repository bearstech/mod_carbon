The missing link between collectd and graphite
==============================================

Collectd 5.1 has a graphite plugins. For other users stucks with stable version, here is a simple python module.

It's an early release with hardcoded parameters.
Please, start carbon daemon first.

Install
-------

Load the python plugin.

    <LoadPlugin python>
        Globals true
    </LoadPlugin>

And instantiate it

    <Plugin python>
        ModulePath "/absolute/path/to/mod_carbon/"
        LogTraces true
        Interactive false
        import mod_carbon
    </Plugin>

Licence
-------

MIT
