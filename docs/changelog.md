---
layout: default
title: Changelos
nav_order: 4
---

# Changelog

Relevant changes
{: .fs-6 .fw-300 }

---

**2019-06-23**
```
*inside an hook callback you can now use this.postContextSetup(function() {});
the callback will be dispatched after the backend have the context in place (as standard hooks callbacks are executed before dispatching the data to the backend). This was need to automate the emulator through js api which require backend context in place
* added a third object to Interceptor.attach(ptr, callback, options) which takes an dictonary of options.
unique public option actually available is details true/false. certain hooks bring trouble parsing additional informations such as backtrace and symbols. this collect just the base information needed by the backend
* fix emulator start/setup/step from js api
* emulator: move memory accesses and maps to own tabs
```
----
**2019-06-22**
```
* added moar keywords to auto completer and inputs
* fix wrong behaviors when running native on loads callbacks
* added detach to this object in interceptor callbacks for quick detaching
* totally removed session save and restore. dwarf won't exit anymore if process terminate but now we can pick what to do, including restarting with the previous agent
initial integration of r2 (wip)
* a lot of dead code cleanup
* improved emulation, added steps till functions call or jump and ability to pick arch and mode
* added debug symbols to jump/call addresses in disasm panel
* added a new UI tab next to console for events from js to prevent spam on js console
* other fixes here and there
```