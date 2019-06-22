---
layout: default
title: Q&A and quick examples
nav_order: 5
---


{: .no_toc }


Be creative!
{: .fs-6 .fw-300 }

{: .no_toc .text-delta }

{:toc}

{: .no_toc }

---

> **Can I use my frida scripts inside Dwarf?**

> yes, by using the button "ƒ" next to the console you can pop the javascript editor and inject your scripts

---

> **How can I get the pointers of my target functions?**

> there are several ways. each dwarf input accepts javascript with either frida or dwarf api. you can use one of the 
various api (i.e enumerateExports | enumerateImports | enumerateSymbols) on your target module or use the disassembly
view to dig through ASM

---

# Scripting examples

## Hooking and break
```javascript
const open = api.findExport('open');
api.hookNative(open, function() {
  // registers held in this.context object and shown in UI
  
  // additional logic
  if (this.context.r0.readUtf8String() === '/my/path') {
      this.context.r0.writeUtf8String('nop');
  }
  
  // the thread will break allowing addition ui operation
});
```

Here if we want to break only at certain conditions - eventually editable through UI as well
```javascript
const open = api.findExport('open');
api.hookNative(open, function() {
  if (this.context.r0.readUtf8String() === '/my/path') {
      this.context.r0.writeUtf8String('nop');
  } else {
      // by returning -1 in our callback the thread won't be break
      return -1;
  }  
});
```
