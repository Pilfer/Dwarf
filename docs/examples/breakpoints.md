---
layout: default
title: breakpoints
parent: Examples
nav_order: 1
---


{: .no_toc }


Be creative!
{: .fs-6 .fw-300 }

{: .no_toc .text-delta }

{:toc}

{: .no_toc }


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
