     var virCookies={"Triaquae_Hostname":1,"System_Hostname":1,"System_Ip":1,"Device_Type":1,"Device_Model":1,"System_kernel":1,
         "Ethernet_Interface":1,"Memory_Slots_Number":1,"Memory_Slots_All":0,"Physical_Memory":1,"Logical_Cpu_Cores":1,
         "Physical_Cpu_Cores":1, "Physical_Cpu_Model":1,"Physical_Cpu_MHz":1,"System_Version":1, "Hard_Disk":1,
         "System_Mac":1, "System_Hostid":0, "System_Swap":1, "Device_Sn":1, "Asset_Number":1, "Note1":0, "Note2":0, "Note3":0,"Check_Time":1};
     $(document).ready(function(){
         var i=0;
         $.each(virCookies,function(name,val){
             var inHtml="<div><input type=\"checkbox\" id=\"ch_"+name
                     +"\" "+(val?"checked=\"checked\"":"")
                     +"\" onclick=\"show_hide_column("
                     +i+")\" /><label for=\"ch_"+name+"\" style=\"display:inline; padding-left:10px\">"+name+"</label></div>";
             $("#colsDiv").append(inHtml);
             if(!val){
                 $("td:eq("+i+")","tr","table[id=col-filter]").hide();
                 $("th:eq("+i+")","tr","table[id=col-filter]").hide();
             }
             i++;
         });
     });

      function show_hide_column(index){
        /*
          $("td:eq("+index+")","tr","table[id=col-filter]").toggle();
        */
         $("td:eq("+index+")","tr","table[id=col-filter").toggle();
         $("th:eq("+index+")","tr","table[id=col-filter").toggle();
      }

      function show_div(){
         /*alert($("td","tr:eq(0)","table[id=col-filter]").width());*/

         $("#colsDiv").css({left:(event.clientX-2)+"px",top:(event.clientY-1)+"px",zIndex:"10",position:"fixed"}).show(0,function(){
             $("#colsDiv").bind("mouseleave",function(){
                 $("#colsDiv").hide();
             });
             //e.addEventListener("click");
         });
      }

