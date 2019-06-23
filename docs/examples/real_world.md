---
layout: default
title: mixed real world
parent: Examples
nav_order: 2
---


{: .no_toc }


Be creative!
{: .fs-6 .fw-300 }

{: .no_toc .text-delta }

{:toc}

{: .no_toc }


# Scripting examples

stepping module initializations, chain a break to an offset and start emulation
```javascript
api.hookNativeOnLoad('xxx.so', function () {
    // grab the base
    const base = this.context.r2;
    // log to ui
    console.log('base =: ' + base);
    // remove the breakpoint - single shoot
    api.deleteHook('xxx.so');

    // declare target ptr
    const payloadRecv = base.add(0x630FAE).add(1);
    // hook it
    api.hookNative(payloadRecv, function () {
        console.log('hook in');
        
        // our callback is dispatched before the backend context is ready
        // we can perform additional operation after the py backend is in place
        // in example, starting the emulator - which needs the py context
        this.postContextSetup(function () {
            // remove this hook
            api.deleteHook(payloadRecv);
            
            // setup the emulator and step the next function
            emulator.setup(null, 'arm', 'thumb');
            emulator.stepFunction();
        });
    }, {
        // no backtrace, symbols to UI
        details: false
    });

    // do not break - continue
    return -1;
});
```