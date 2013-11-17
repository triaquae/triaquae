/*
*
* Placeholder.js minified version 1.1.1
* Creates placeholder on inputs/textareas for browsers that don't support it (well, IE...)
*
* @ Created by Guillaume Gaubert
* @ http://widgetulous.com/placeholderjs/
* @ © 2011 Guillaume Gaubert
*
* @ Default use :
*   Placeholder.init();
*
*/

Placeholder={defaultSettings:{normal:'#000000',placeholder:'#C0C0C0',wait:false,classFocus:'',classBlur:''},init:function(a){if(a){for(var b in a){Placeholder.defaultSettings[b]=a[b]}}var c=document.getElementsByTagName("input");var d=document.getElementsByTagName("textarea");var e=Placeholder.utils.concat(c,d);for(var i=0;i<e.length;i++){var g=e[i].getAttribute("placeholder");if(g&&e[i].type=="text"||e[i].type=="password"||e[i].type=="textarea"){var h=e[i];h.onclick=function(){Placeholder.onSelected(this)};h.onfocus=function(){};h.onblur=function(){Placeholder.unSelected(this)};if(Placeholder.defaultSettings.wait){h.onkeypress=function(){Placeholder.onType(this)}}Placeholder.style.inactive(h);h.value=g;var j=document.getElementsByTagName('form');for(var f=0;f<j.length;f++){if(j[f]){var k=j[f].children;if(Placeholder.utils.contains(k,h)){j[f].onsubmit=function(){Placeholder.submitted(this)}}}}}}},onSelected:function(a){if(Placeholder.defaultSettings.wait==true){if(a.value==a.getAttribute('placeholder')){Placeholder.utils.caret(a)}}else{if(a.value==a.getAttribute('placeholder')){a.value=''}Placeholder.style.normal(a)}},onType:function(a){var b=a.getAttribute('placeholder');a.value=a.value.replace(b,'');if(a.value.length<=0){Placeholder.style.inactive(a);a.value=b;Placeholder.utils.caret(a)}else{Placeholder.style.normal(a)}},unSelected:function(a){if(a.value.length<=0){Placeholder.style.inactive(a);a.value=a.getAttribute("placeholder")}},submitted:function(a){var b=a.children;for(var i=0;i<b.length;i++){if(b[i]){var c=b[i];if(c.tagName.toLowerCase()=="input"||c.tagName.toLowerCase()=="textarea"){if(c.value==c.getAttribute('placeholder')){c.value=""}}}}},style:{normal:function(a){if(Placeholder.defaultSettings.classFocus){a.className=Placeholder.defaultSettings.classFocus}else{a.style.color=Placeholder.defaultSettings.normal}},inactive:function(a){if(Placeholder.defaultSettings.classBlur){a.className=Placeholder.defaultSettings.classBlur}else{a.style.color=Placeholder.defaultSettings.placeholder}}},utils:{contains:function(a,b){for(var i=0;i<a.length;i++){if(a[i]){if(a[i]==b){return true}}}return false},concat:function(a,b){var c=[];for(var i=0;i<a.length;i++){if(a[i]){c.push(a[i])}}for(var i=0;i<b.length;i++){if(b[i]){c.push(b[i])}}return c},caret:function(a){if(a.setSelectionRange){a.focus();a.setSelectionRange(0,0)}else if(a.createTextRange){var b=a.createTextRange();b.collapse(true);b.moveEnd('character',0);b.moveStart('character',0);b.select()}}}};