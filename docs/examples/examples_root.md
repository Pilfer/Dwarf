---
layout: default
title: Examples
nav_order: 5
has_children: true
permalink: docs/examples
---

# Examples
{: .no_toc }

Be creative!
{: .fs-6 .fw-300 }

{: .no_toc .text-delta }

---

> **Can I use my frida scripts inside Dwarf?**

> yes, by using the button "ƒ" next to the console you can pop the javascript editor and inject your scripts

---

> **How can I get the pointers of my target functions?**

> there are several ways. each dwarf input accepts javascript with either frida or dwarf api. you can use one of the 
various api (i.e enumerateExports | enumerateImports | enumerateSymbols) on your target module or use the disassembly
view to dig through ASM
