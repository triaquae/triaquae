/*         
           __                   .__        
           |__|____ __________  _|__| ______
           |  \__  \\_  __ \  \/ /  |/  ___/
           |  |/ __ \|  | \/\   /|  |\___ \ 
           /\__|  (____  /__|    \_/ |__/____  >
           \______|    \/                    \/ 

           Copyright 2013 - Jarvis : Smart Admin Template version 1.9.4

 * This is part of an item on wrapbootstrap.com
 * https://wrapbootstrap.com/user/myorange
 * ==================================


 Table of Contents
 ---------------------------------------------------------------

 - Right Side Bar
 - Turn On RTL Menu
 - Collapse Menu
 - Set Vars
 - On Page Load
 - isMobile
 - Responsive nav 
 - Widgets Desktop
 - widgets Mobile
 - Reset widgets script
 - Calendar
 - JarvisGuage
 - Flot charts
 - Sparklines setup
 - Progress bar
 - Toastr setup
 - Functions for idevice
 - All button functions
 - Logout
 - Slimscroll
 - Easypie
 - Randomize easy pie
 - Chat message
 - Bootbox
 - Enable Select2
 - Setup_datepicker_demo
 - Setup_masked_input
 - Setup_masked_input
 - Setup_timepicker
 - Setup_uislider
 - Validation_setup_demo
 - Setup_wizard_demo
 - Setup checkedin tables
 - Activate_bt_accordion_hack
 - Setup ios button demo
 - Window.resize functions
 - Window.load functions

*/

/* ---------------------------------------------------------------------- */
/*	Set Vars
/* ---------------------------------------------------------------------- */

/* collapse menu */
$.collapse_menu = false;  // Sets up the option for collapsing the left hand pane

/* right side bar */
$.right_bar = true;  // If you wish to disable the right side bar from displaying

$.rtl = false;

/* used with chatbox demo */
$.istying = $('textarea#chat-box-textarea');

/* chart colors default */
var $chrt_border_color = "#efefef";
var $chrt_grid_color = "#DDD"
var $chrt_main = "#E24913";			/* red       */
var $chrt_second = "#4b99cb";		/* blue      */
var $chrt_third = "#FF9F01";		/* orange    */
var $chrt_fourth = "#87BA17";		/* green     */
var $chrt_fifth = "#BD362F";		/* dark red  */
var $chrt_mono = "#000";

//turn this on if your browser supports audio

/*var $pop_sound = new Audio("sounds/sound-pop-clear.mp3"); // buffers automatically when created
  var $smallbox = new Audio("sounds/smallbox.mp3"); // buffers automatically when created
  var $messagebox = new Audio("sounds/messagebox.mp3"); // buffers automatically when created
  var $bigbox = new Audio("sounds/bigbox.mp3"); // buffers automatically when created*/


/* ---------------------------------------------------------------------- */
/*	On Page Load
/* ---------------------------------------------------------------------- */

$(document).ready( function() {   

  /* right side bar */
  right_side_bar();

  /* switch menu */
  turn_on_rtl_menu();

  /* collapse menu */
  collapse_menu();

  /* navigation for mobile - it is recommended that you only execute this if mobile is true */
  setup_responsive_nav();

  /* draw flot charts */
  setup_flots();

  /* draw calendar */
  setup_calendar();

  /* find #second-menu-js and apply accordion menu function */
  setup_accordion_menu();

  /* setup toastr responsive alerts */
  setup_toastr();

  /* slimscroll */
  setup_slimscroll();

  /* expand search input on focus */
  execute_idevice_functions();	

  /* detect if mobile */
  isMobile() 

    /* all buttons */
    setup_all_buttons()

    /* draw easy pie */
    setup_easypie();

  /* activate sparklines */
  setup_sparklines();

  /*progress bar animate*/
  progressbar_animate();

  /* wysihtml5 editor*/
  setup_wysihtml5();

  /* start justguage */
  setup_jarvisGuage();

  /* start chatbox */
  setup_chatbox_demo();

  /* start bootbox */
  setup_bootbox_demo();

  /* datepicker for forms */
  setup_datepicker_demo();

  /* colorpicker for forms */
  setup_colorpicker_demo();

  /* masked input */
  setup_masked_input();

  /* setup_timepicker */
  setup_timepicker();

  /* setup_uislider */
  setup_uislider();

  /* validation_setup_demo */
  validation_setup_demo();

  /* wizard demo */
  setup_wizard_demo();	

  /* tables with checked in checkboxes */
  setup_checkedin_tables_demo();

  /* custom form elements */
  setup_custom_form_elements();

}); 

/* end on page load */

/* ---------------------------------------------------------------------- */
/*	isMobile
/* ---------------------------------------------------------------------- */

/** NOTE: Notice we have seperated funtion calls based on user platform. 
  This significantly cuts down on memory usage and prolongs a healthy 
  user experience. 
 **/

function isMobile() {
  /* so far this is covering most hand held devices */
  var ismobile = (/iphone|ipad|ipod|android|blackberry|mini|windows\sce|palm/i.test(navigator.userAgent.toLowerCase()));	
  if(!ismobile){
    //console.log("NOT mobile version - message from config.js");

    /* widgets for desktop */
    setup_widgets_desktop();

    /* inline datepicker - appears on aside (right) */
    $('#datepicker').datepicker();

  } else {
    //console.log("IS mobile version - message from config.js");

    /* widgets for desktop */
    setup_widgets_mobile();
  }
}

/* end isMobile */

/* ---------------------------------------------------------------------- */
/*	Right Side Bar
/* ---------------------------------------------------------------------- */

function right_side_bar(){

  if ($.right_bar == false) {
    $('html').addClass('no-right-bar');
  }

}

/* ---------------------------------------------------------------------- */
/*	Turn On RTL Menu
/* ---------------------------------------------------------------------- */

function turn_on_rtl_menu(){

  if ($.rtl == true) {
    $('aside').css('float','right');
    $('aside.right').css('right','auto');
    $('#page-content').css('margin-left','249px') // this should be a class
  }

}

/* ---------------------------------------------------------------------- */
/*	Collapse Menu
/* ---------------------------------------------------------------------- */

function collapse_menu(){

  if ($.collapse_menu == true) {
    $('#page-header').prepend('<a class="btn btn-navbar" id="response-btn"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </a>')
  }

}

/* end Collapse Menu */

/* ---------------------------------------------------------------------- */
/*	Responsive nav 
/* ---------------------------------------------------------------------- */

function setup_responsive_nav() {

  /* build responsive menu in dropdown select */		
  selectnav('accordion-menu-js', {
    label: 'Quick Menu ',
  nested: true,
  indent: '-'
  });

}

/* end responsive nav */

/* ---------------------------------------------------------------------- */
/*	Widgets Desktop
/* ---------------------------------------------------------------------- */	

function setup_widgets_desktop() {

  if ($('#widget-grid').length){

    $('#widget-grid').jarvisWidgets({	

      grid: 'article',
    widgets: '.jarviswidget',
    localStorage: true,
    deleteSettingsKey: '#deletesettingskey-options',
    settingsKeyLabel: 'Reset settings?',
    deletePositionKey: '#deletepositionkey-options',
    positionKeyLabel: 'Reset position?',
    sortable: true,
    buttonsHidden: false,
    toggleButton: true,
    toggleClass: 'min-10 | plus-10',
    toggleSpeed: 200,
    onToggle: function(){},
    deleteButton: true,
    deleteClass: 'trashcan-10',
    deleteSpeed: 200,
    onDelete: function(){},
    editButton: true,
    editPlaceholder: '.jarviswidget-editbox',
    editClass: 'pencil-10 | edit-clicked',
    editSpeed: 200,
    onEdit: function(){},
    fullscreenButton: true,
    fullscreenClass: 'fullscreen-10 | normalscreen-10',	
    fullscreenDiff: 3,		
    onFullscreen: function(){},
    customButton: false,
    customClass: 'folder-10 | next-10',
    customStart: function(){ alert('Hello you, this is a custom button...') },
    customEnd: function(){ alert('bye, till next time...') },
    buttonOrder: '%refresh% %delete% %custom% %edit% %fullscreen% %toggle%',
    opacity: 1.0,
    dragHandle: '> header',
    placeholderClass: 'jarviswidget-placeholder',
    indicator: true,
    indicatorTime: 600,
    ajax: true,
    timestampPlaceholder:'.jarviswidget-timestamp',
    timestampFormat: 'Last update: %m%/%d%/%y% %h%:%i%:%s%',
    refreshButton: true,
    refreshButtonClass: 'refresh-10',
    labelError:'Sorry but there was a error:',
    labelUpdated: 'Last Update:',
    labelRefresh: 'Refresh',
    labelDelete: 'Delete widget:',
    afterLoad: function(){},
    rtl: false

    });

  } // end if

}

/* end widgets desktop */

/* ---------------------------------------------------------------------- */
/*	Widgets Mobile
/* ---------------------------------------------------------------------- */

function setup_widgets_mobile() {	

  if ($('#widget-grid').length){

    $('#widget-grid').jarvisWidgets({	

      grid: 'article',
    widgets: '.jarviswidget',
    localStorage: true,
    deleteSettingsKey: '#deletesettingskey-options',
    settingsKeyLabel: 'Reset settings?',
    deletePositionKey: '#deletepositionkey-options',
    positionKeyLabel: 'Reset position?',
    sortable: false, // sorting disabled for mobile
    buttonsHidden: false,
    toggleButton: true,
    toggleClass: 'min-10 | plus-10',
    toggleSpeed: 200,
    onToggle: function(){},
    deleteButton: false,
    deleteClass: 'trashcan-10',
    deleteSpeed: 200,
    onDelete: function(){},
    editButton: true,
    editPlaceholder: '.jarviswidget-editbox',
    editClass: 'pencil-10 | edit-clicked',
    editSpeed: 200,
    onEdit: function(){},
    fullscreenButton: false,
    fullscreenClass: 'fullscreen-10 | normalscreen-10',	
    fullscreenDiff: 3,		
    onFullscreen: function(){},
    customButton: false, // custom button disabled for mobile
    customClass: 'folder-10 | next-10',
    customStart: function(){ alert('Hello you, this is a custom button...') },
    customEnd: function(){ alert('bye, till next time...') },
    buttonOrder: '%refresh% %delete% %custom% %edit% %fullscreen% %toggle%',
    opacity: 1.0,
    dragHandle: '> header',
    placeholderClass: 'jarviswidget-placeholder',
    indicator: true,
    indicatorTime: 600,
    ajax: true,
    timestampPlaceholder:'.jarviswidget-timestamp',
    timestampFormat: 'Last update: %m%/%d%/%y% %h%:%i%:%s%',
    refreshButton: true,
    refreshButtonClass: 'refresh-10',
    labelError:'Sorry but there was a error:',
    labelUpdated: 'Last Update:',
    labelRefresh: 'Refresh',
    labelDelete: 'Delete widget:',
    afterLoad: function(){},
    rtl: false

    });

  }// end if

}

/* end widgets Mobile */

/* ---------------------------------------------------------------------- */
/*	Reset widgets script
/* ---------------------------------------------------------------------- */

function resetWidget() {

  var cls = confirm("Would you like to RESET all your saved widgets and clear LocalStorage?");
  if(cls && localStorage){
    localStorage.clear();
    //alert('Local storage has been cleared! Refreshing page...');
    location.reload();
  }

}

/* end reset widgets script */

/* ---------------------------------------------------------------------- */
/*	set up accordion menu
/* ---------------------------------------------------------------------- */	

function setup_accordion_menu () {

  $("#accordion-menu-js").ctAccordion();	
}

/* end setup accordion menu */

/* ---------------------------------------------------------------------- */
/*	Calendar
/* ---------------------------------------------------------------------- */

function setup_calendar() {

  if ($("#calendar").length) {
    var date = new Date();
    var d = date.getDate();
    var m = date.getMonth();
    var y = date.getFullYear();

    var calendar = $('#calendar').fullCalendar({
      header: {
        left: 'title', //,today
        center: 'prev, next, today',
        right: 'month, agendaWeek, agenDay' //month, agendaDay, 
      },
        selectable: true,
        selectHelper: true,
        select: function(start, end, allDay) {
          var title = prompt('Event Title:');
          if (title) {
            calendar.fullCalendar('renderEvent',
              {
                title: title,
              start: start,
              end: end,
              allDay: allDay
              },
              true // make the event "stick"
              );
          }
          calendar.fullCalendar('unselect');
        },

        editable: true,
        events: [
        /*
        {
          title: 'All Day Event',
          start: new Date(y, m, 1)
        },
        {
          title: 'Long Event',
          start: new Date(y, m, d-5),
          end: new Date(y, m, d-2)
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: new Date(y, m, d-3, 16, 0),
          allDay: false
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: new Date(y, m, d+4, 16, 0),
          allDay: false
        },
        {
          title: 'Meeting',
          start: new Date(y, m, d, 10, 30),
          allDay: false
        },
        {
          title: 'Lunch',
          start: new Date(y, m, d, 12, 0),
          end: new Date(y, m, d, 14, 0),
          allDay: false
        },
        {
          title: 'Birthday Party',
          start: new Date(y, m, d+1, 19, 0),
          end: new Date(y, m, d+1, 22, 30),
          allDay: false
        },
        {
          title: 'Click for Google',
          start: new Date(y, m, 28),
          end: new Date(y, m, 29),
          url: 'http://google.com/'
        }
        */
    ]
    });

  };

  /* hide default buttons */
  $('.fc-header-right, .fc-header-center').hide();

}

/* end calendar */

/* ---------------------------------------------------------------------- */
/*	JarvisGuage
/* ---------------------------------------------------------------------- */	

function setup_jarvisGuage() {

  if ($('#gague-chart').length) {
    var g1, g2, g3, g4, g5, g6;

    window.onload = function() {
      var g1 = new JustGage({
        id : "g1",
          value : getRandomInt(0, 100),
          min : 0,
          max : 100,
          title : "Custom Width",
          label : "",
          //valueFontColor : "#ed1c24",
          gaugeWidthScale : 0.2
      });

      var g2 = new JustGage({
        id : "g2",
          value : getRandomInt(0, 100),
          min : 0,
          max : 100,
          title : "Custom Shadow",
          label : "",
          shadowOpacity : 1,
          shadowSize : 0,
          shadowVerticalOffset : 10
      });

      var g3 = new JustGage({
        id : "g3",
          value : getRandomInt(0, 100),
          min : 0,
          max : 100,
          title : "Custom Colors",
          label : "",
          levelColors : ["#00fff6", "#ff00fc", $chrt_third]
      });

      var g4 = new JustGage({
        id : "g4",
          value : getRandomInt(0, 100),
          min : 0,
          max : 100,
          title : "Hide Labels",
          showMinMax : false
      });

      var g5 = new JustGage({
        id : "g5",
          value : getRandomInt(0, 100),
          min : 0,
          max : 100,
          title : "Animation Type",
          label : "",
          startAnimationTime : 2000,
          startAnimationType : ">",
          refreshAnimationTime : 1000,
          refreshAnimationType : "bounce"
      });

      var g6 = new JustGage({
        id : "g6",
          value : getRandomInt(0, 100),
          min : 0,
          max : 100,
          title : "Minimal",
          label : "",
          showMinMax : false,
          levelColors : [$chrt_second],
          showInnerShadow : false,
          startAnimationTime : 1,
          startAnimationType : "linear",
          refreshAnimationTime : 1,
          refreshAnimationType : "linear"
      });

      setInterval(function() {
        g1.refresh(getRandomInt(0, 100));
        g2.refresh(getRandomInt(0, 100));
        g3.refresh(getRandomInt(0, 100));
        g4.refresh(getRandomInt(0, 100));
        g5.refresh(getRandomInt(0, 100));
        g6.refresh(getRandomInt(0, 100));
      }, 2500);
    };
  } // end if

}

/* end JarvisGague */  

/* ---------------------------------------------------------------------- */
/*	Flot charts
/* ---------------------------------------------------------------------- */	

function setup_flots() {

  /* sales chart */

  if ($("#saleschart").length) {

    var d = [[1196463600000, 0], [1196550000000, 0], [1196636400000, 0], [1196722800000, 77], [1196809200000, 3636], [1196895600000, 3575], [1196982000000, 2736], [1197068400000, 1086], [1197154800000, 676], [1197241200000, 1205], [1197327600000, 906], [1197414000000, 710], [1197500400000, 639], [1197586800000, 540], [1197673200000, 435], [1197759600000, 301], [1197846000000, 575], [1197932400000, 481], [1198018800000, 591], [1198105200000, 608], [1198191600000, 459], [1198278000000, 234], [1198364400000, 1352], [1198450800000, 686], [1198537200000, 279], [1198623600000, 449], [1198710000000, 468], [1198796400000, 392], [1198882800000, 282], [1198969200000, 208], [1199055600000, 229], [1199142000000, 177], [1199228400000, 374], [1199314800000, 436], [1199401200000, 404], [1199487600000, 253], [1199574000000, 218], [1199660400000, 476], [1199746800000, 462], [1199833200000, 500], [1199919600000, 700], [1200006000000, 750], [1200092400000, 600], [1200178800000, 500], [1200265200000, 900], [1200351600000, 930], [1200438000000, 1200], [1200524400000, 980], [1200610800000, 950], [1200697200000, 900], [1200783600000, 1000], [1200870000000, 1050], [1200956400000, 1150], [1201042800000, 1100], [1201129200000, 1200], [1201215600000, 1300], [1201302000000, 1700], [1201388400000, 1450], [1201474800000, 1500], [1201561200000, 546], [1201647600000, 614], [1201734000000, 954], [1201820400000, 1700], [1201906800000, 1800], [1201993200000, 1900], [1202079600000, 2000], [1202166000000, 2100], [1202252400000, 2200], [1202338800000, 2300], [1202425200000, 2400], [1202511600000, 2550], [1202598000000, 2600], [1202684400000, 2500], [1202770800000, 2700], [1202857200000, 2750], [1202943600000, 2800], [1203030000000, 3245], [1203116400000, 3345], [1203202800000, 3000], [1203289200000, 3200], [1203375600000, 3300], [1203462000000, 3400], [1203548400000, 3600], [1203634800000, 3700], [1203721200000, 3800], [1203807600000, 4000], [1203894000000, 4500]];

    for (var i = 0; i < d.length; ++i)
      d[i][0] += 60 * 60 * 1000;

    function weekendAreas(axes) {
      var markings = [];
      var d = new Date(axes.xaxis.min);
      // go to the first Saturday
      d.setUTCDate(d.getUTCDate() - ((d.getUTCDay() + 1) % 7))
        d.setUTCSeconds(0);
      d.setUTCMinutes(0);
      d.setUTCHours(0);
      var i = d.getTime();
      do {
        // when we don't set yaxis, the rectangle automatically
        // extends to infinity upwards and downwards
        markings.push({
          xaxis : {
            from : i,
          to : i + 2 * 24 * 60 * 60 * 1000
          }
        });
        i += 7 * 24 * 60 * 60 * 1000;
      } while (i < axes.xaxis.max);

      return markings;
    }

    var options = {
      xaxis : {
        mode : "time",
        tickLength : 5
      },
      series : {
        lines : {
          show : true,
          lineWidth : 1,
          fill : true,
          fillColor : {
            colors : [{
              opacity : 0.1
            }, {
              opacity : 0.15
            }]
          }
        },
        //points: { show: true },
        shadowSize : 0
      },
      selection : {
        mode : "x"
      },
      grid : {
        hoverable : true,
        clickable : true,
        tickColor : $chrt_border_color,
        borderWidth : 0,
        borderColor : $chrt_border_color,
      },
      tooltip : true,
      tooltipOpts : {
        content : "Your sales for <b>%x</b> was <span>$%y</span>",
        dateFormat : "%y-%0m-%0d",
        defaultTheme : false
      },
      colors : [$chrt_second],

    };

    var plot = $.plot($("#saleschart"), [d], options);
  };

  /* end sales chart */
  /* Sin chart */

  if ($("#sin-chart").length) {
    var sin = [], cos = [];
    for (var i = 0; i < 16; i += 0.5) {
      sin.push([i, Math.sin(i)]);
      cos.push([i, Math.cos(i)]);
    }

    var plot = $.plot($("#sin-chart"), [{
      data : sin,
        label : "sin(x)"
    }, {
      data : cos,
        label : "cos(x)"
    }], {
      series : {
        lines : {
          show : true
        },
        points : {
          show : true
        }
      },
        grid : {
          hoverable : true,
        clickable : true,
        tickColor : $chrt_border_color,
        borderWidth : 0,
        borderColor : $chrt_border_color,
        },
        tooltip : true,
        tooltipOpts : {
          //content : "Value <b>$x</b> Value <span>$y</span>",
          defaultTheme : false
        },
        colors : [$chrt_second, $chrt_fourth],
        yaxis : {
          min : -1.1,
          max : 1.1
        },
        xaxis : {
          min : 0,
          max : 15
        }
    });

    $("#sin-chart").bind("plotclick", function(event, pos, item) {
      if (item) {
        $("#clickdata").text("You clicked point " + item.dataIndex + " in " + item.series.label + ".");
        plot.highlight(item.series, item.datapoint);
      }
    });
  }

  /* end sin chart */

  /* bar chart */

  if ($("#bar-chart").length) {

    var data1 = [];
    for (var i = 0; i <= 12; i += 1)
      data1.push([i, parseInt(Math.random() * 30)]);

    var data2 = [];
    for (var i = 0; i <= 12; i += 1)
      data2.push([i, parseInt(Math.random() * 30)]);

    var data3 = [];
    for (var i = 0; i <= 12; i += 1)
      data3.push([i, parseInt(Math.random() * 30)]);

    var ds = new Array();

    ds.push({
      data : data1,
      bars : {
        show : true,
      barWidth : 0.2,
      order : 1,
      }
    });
    ds.push({
      data : data2,
      bars : {
        show : true,
      barWidth : 0.2,
      order : 2
      }
    });
    ds.push({
      data : data3,
      bars : {
        show : true,
      barWidth : 0.2,
      order : 3
      }
    });

    //Display graph
    $.plot($("#bar-chart"), ds, {
      colors : [$chrt_second, $chrt_fourth, "#666", "#BBB"],
      grid : {
        show : true,
      hoverable : true,
      clickable : true,
      tickColor : $chrt_border_color,
      borderWidth : 0,
      borderColor : $chrt_border_color,
      },
      legend : true,
      tooltip : true,
      tooltipOpts : {
        content : "<b>%x</b> = <span>%y</span>",
      defaultTheme : false
      }

    });

  }

  /* end bar chart */

  /* bar-chart-h */
  if ($("#bar-chart-h").length) {
    //Display horizontal graph
    var d1_h = [];
    for (var i = 0; i <= 3; i += 1)
      d1_h.push([parseInt(Math.random() * 30), i]);

    var d2_h = [];
    for (var i = 0; i <= 3; i += 1)
      d2_h.push([parseInt(Math.random() * 30), i]);

    var d3_h = [];
    for (var i = 0; i <= 3; i += 1)
      d3_h.push([parseInt(Math.random() * 30), i]);

    var ds_h = new Array();
    ds_h.push({
      data : d1_h,
      bars : {
        horizontal : true,
      show : true,
      barWidth : 0.2,
      order : 1,
      }
    });
    ds_h.push({
      data : d2_h,
      bars : {
        horizontal : true,
      show : true,
      barWidth : 0.2,
      order : 2
      }
    });
    ds_h.push({
      data : d3_h,
      bars : {
        horizontal : true,
      show : true,
      barWidth : 0.2,
      order : 3
      }
    });

    // display graph
    $.plot($("#bar-chart-h"), ds_h, {
      colors : [$chrt_second, $chrt_fourth, "#666", "#BBB"],
      grid : {
        show : true,
      hoverable : true,
      clickable : true,
      tickColor : $chrt_border_color,
      borderWidth : 0,
      borderColor : $chrt_border_color,
      },
      legend : true,
      tooltip : true,
      tooltipOpts : {
        content : "<b>%x</b> = <span>%y</span>",
      defaultTheme : false
      }
    });

  } 

  /* end bar-chart-h

  /* fill chart */

  if ($("#fill-chart").length) {
    var males = {
      '15%' : [[2, 88.0], [3, 93.3], [4, 102.0], [5, 108.5], [6, 115.7], [7, 115.6], [8, 124.6], [9, 130.3], [10, 134.3], [11, 141.4], [12, 146.5], [13, 151.7], [14, 159.9], [15, 165.4], [16, 167.8], [17, 168.7], [18, 169.5], [19, 168.0]],
      '90%' : [[2, 96.8], [3, 105.2], [4, 113.9], [5, 120.8], [6, 127.0], [7, 133.1], [8, 139.1], [9, 143.9], [10, 151.3], [11, 161.1], [12, 164.8], [13, 173.5], [14, 179.0], [15, 182.0], [16, 186.9], [17, 185.2], [18, 186.3], [19, 186.6]],
      '25%' : [[2, 89.2], [3, 94.9], [4, 104.4], [5, 111.4], [6, 117.5], [7, 120.2], [8, 127.1], [9, 132.9], [10, 136.8], [11, 144.4], [12, 149.5], [13, 154.1], [14, 163.1], [15, 169.2], [16, 170.4], [17, 171.2], [18, 172.4], [19, 170.8]],
      '10%' : [[2, 86.9], [3, 92.6], [4, 99.9], [5, 107.0], [6, 114.0], [7, 113.5], [8, 123.6], [9, 129.2], [10, 133.0], [11, 140.6], [12, 145.2], [13, 149.7], [14, 158.4], [15, 163.5], [16, 166.9], [17, 167.5], [18, 167.1], [19, 165.3]],
      'mean' : [[2, 91.9], [3, 98.5], [4, 107.1], [5, 114.4], [6, 120.6], [7, 124.7], [8, 131.1], [9, 136.8], [10, 142.3], [11, 150.0], [12, 154.7], [13, 161.9], [14, 168.7], [15, 173.6], [16, 175.9], [17, 176.6], [18, 176.8], [19, 176.7]],
      '75%' : [[2, 94.5], [3, 102.1], [4, 110.8], [5, 117.9], [6, 124.0], [7, 129.3], [8, 134.6], [9, 141.4], [10, 147.0], [11, 156.1], [12, 160.3], [13, 168.3], [14, 174.7], [15, 178.0], [16, 180.2], [17, 181.7], [18, 181.3], [19, 182.5]],
      '85%' : [[2, 96.2], [3, 103.8], [4, 111.8], [5, 119.6], [6, 125.6], [7, 131.5], [8, 138.0], [9, 143.3], [10, 149.3], [11, 159.8], [12, 162.5], [13, 171.3], [14, 177.5], [15, 180.2], [16, 183.8], [17, 183.4], [18, 183.5], [19, 185.5]],
      '50%' : [[2, 91.9], [3, 98.2], [4, 106.8], [5, 114.6], [6, 120.8], [7, 125.2], [8, 130.3], [9, 137.1], [10, 141.5], [11, 149.4], [12, 153.9], [13, 162.2], [14, 169.0], [15, 174.8], [16, 176.0], [17, 176.8], [18, 176.4], [19, 177.4]]
    };

    var females = {
      '15%' : [[2, 84.8], [3, 93.7], [4, 100.6], [5, 105.8], [6, 113.3], [7, 119.3], [8, 124.3], [9, 131.4], [10, 136.9], [11, 143.8], [12, 149.4], [13, 151.2], [14, 152.3], [15, 155.9], [16, 154.7], [17, 157.0], [18, 156.1], [19, 155.4]],
      '90%' : [[2, 95.6], [3, 104.1], [4, 111.9], [5, 119.6], [6, 127.6], [7, 133.1], [8, 138.7], [9, 147.1], [10, 152.8], [11, 161.3], [12, 166.6], [13, 167.9], [14, 169.3], [15, 170.1], [16, 172.4], [17, 169.2], [18, 171.1], [19, 172.4]],
      '25%' : [[2, 87.2], [3, 95.9], [4, 101.9], [5, 107.4], [6, 114.8], [7, 121.4], [8, 126.8], [9, 133.4], [10, 138.6], [11, 146.2], [12, 152.0], [13, 153.8], [14, 155.7], [15, 158.4], [16, 157.0], [17, 158.5], [18, 158.4], [19, 158.1]],
      '10%' : [[2, 84.0], [3, 91.9], [4, 99.2], [5, 105.2], [6, 112.7], [7, 118.0], [8, 123.3], [9, 130.2], [10, 135.0], [11, 141.1], [12, 148.3], [13, 150.0], [14, 150.7], [15, 154.3], [16, 153.6], [17, 155.6], [18, 154.7], [19, 153.1]],
      'mean' : [[2, 90.2], [3, 98.3], [4, 105.2], [5, 112.2], [6, 119.0], [7, 125.8], [8, 131.3], [9, 138.6], [10, 144.2], [11, 151.3], [12, 156.7], [13, 158.6], [14, 160.5], [15, 162.1], [16, 162.9], [17, 162.2], [18, 163.0], [19, 163.1]],
      '75%' : [[2, 93.2], [3, 101.5], [4, 107.9], [5, 116.6], [6, 122.8], [7, 129.3], [8, 135.2], [9, 143.7], [10, 148.7], [11, 156.9], [12, 160.8], [13, 163.0], [14, 165.0], [15, 165.8], [16, 168.7], [17, 166.2], [18, 167.6], [19, 168.0]],
      '85%' : [[2, 94.5], [3, 102.8], [4, 110.4], [5, 119.0], [6, 125.7], [7, 131.5], [8, 137.9], [9, 146.0], [10, 151.3], [11, 159.9], [12, 164.0], [13, 166.5], [14, 167.5], [15, 168.5], [16, 171.5], [17, 168.0], [18, 169.8], [19, 170.3]],
      '50%' : [[2, 90.2], [3, 98.1], [4, 105.2], [5, 111.7], [6, 118.2], [7, 125.6], [8, 130.5], [9, 138.3], [10, 143.7], [11, 151.4], [12, 156.7], [13, 157.7], [14, 161.0], [15, 162.0], [16, 162.8], [17, 162.2], [18, 162.8], [19, 163.3]]
    };

    var dataset = [{
      label : 'female mean',
            data : females['mean'],
            lines : {
              show : true
            },
            color : "rgb(255,50,50)"
    }, {
      id : 'f15%',
         data : females['15%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : false
         },
         color : "rgb(255,50,50)"
    }, {
      id : 'f25%',
         data : females['25%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : 0.2
         },
         color : "rgb(255,50,50)",
         fillBetween : 'f15%'
    }, {
      id : 'f50%',
         data : females['50%'],
         lines : {
           show : true,
           lineWidth : 0.5,
           fill : 0.4,
           shadowSize : 0
         },
         color : "rgb(255,50,50)",
         fillBetween : 'f25%'
    }, {
      id : 'f75%',
         data : females['75%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : 0.4
         },
         color : "rgb(255,50,50)",
         fillBetween : 'f50%'
    }, {
      id : 'f85%',
         data : females['85%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : 0.2
         },
         color : "rgb(255,50,50)",
         fillBetween : 'f75%'
    }, {
      label : 'male mean',
            data : males['mean'],
            lines : {
              show : true
            },
            color : "rgb(50,50,255)"
    }, {
      id : 'm15%',
         data : males['15%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : false
         },
         color : "rgb(50,50,255)"
    }, {
      id : 'm25%',
         data : males['25%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : 0.2
         },
         color : "rgb(50,50,255)",
         fillBetween : 'm15%'
    }, {
      id : 'm50%',
         data : males['50%'],
         lines : {
           show : true,
           lineWidth : 0.5,
           fill : 0.4,
           shadowSize : 0
         },
         color : "rgb(50,50,255)",
         fillBetween : 'm25%'
    }, {
      id : 'm75%',
         data : males['75%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : 0.4
         },
         color : "rgb(50,50,255)",
         fillBetween : 'm50%'
    }, {
      id : 'm85%',
         data : males['85%'],
         lines : {
           show : true,
           lineWidth : 0,
           fill : 0.2
         },
         color : "rgb(50,50,255)",
         fillBetween : 'm75%'
    }]

    $.plot($("#fill-chart"), dataset, {

      xaxis : {
        tickDecimals : 0
      },

    yaxis : {
      tickFormatter : function(v) {
        return v + " cm";
      }
    },

    });
  }

  /* end fill chart */

  /* pie chart */

  if ($('#pie-chart').length) {

    var data_pie = [];
    var series = Math.floor(Math.random() * 10) + 1;
    for (var i = 0; i < series; i++) {
      data_pie[i] = {
        label : "Series" + (i + 1),
        data : Math.floor(Math.random() * 100) + 1
      }
    }

    $.plot($("#pie-chart"), data_pie, {
      series : {
        pie : {
          show : true,
      innerRadius : 0.5,
      radius : 1,
      label : {
        show : false,
      radius : 2 / 3,
      formatter : function(label, series) {
        return '<div style="font-size:11px;text-align:center;padding:4px;color:white;">' + label + '<br/>' + Math.round(series.percent) + '%</div>';
      },
      threshold : 0.1
      }
        }
      },
      legend : {
        show : true,
    noColumns : 1, // number of colums in legend table
    labelFormatter : null, // fn: string -> string
    labelBoxBorderColor : "#000", // border color for the little label boxes
    container : null, // container (as jQuery object) to put legend in, null means default on top of graph
    position : "ne", // position of default legend container within plot
    margin : [5, 10], // distance from grid edge to default legend container within plot
    backgroundColor : "#efefef", // null means auto-detect
    backgroundOpacity : 1 // set to 0 to avoid background
      },
      grid : {
        hoverable : true,
        clickable : true
      },
    });

  }

  /* end pie chart */

  /* site stats chart */

  if ($("#site-stats").length) {

    var pageviews = [[1, 75], [3, 87], [4, 93], [5, 127], [6, 116], [7, 137], [8, 135], [9, 130], [10, 167], [11, 169], [12, 179], [13, 185], [14, 176], [15, 180], [16, 174], [17, 193], [18, 186], [19, 177], [20, 153], [21, 149], [22, 130], [23, 100], [24, 50]];
    var visitors = [[1, 65], [3, 50], [4, 73], [5, 100], [6, 95], [7, 103], [8, 111], [9, 97], [10, 125], [11, 100], [12, 95], [13, 141], [14, 126], [15, 131], [16, 146], [17, 158], [18, 160], [19, 151], [20, 125], [21, 110], [22, 100], [23, 85], [24, 37]];
    //console.log(pageviews)
    var plot = $.plot($("#site-stats"), [{
      data : pageviews,
        label : "Your pageviews"
    }, {
      data : visitors,
        label : "Site visitors"
    }], {
      series : {
        lines : {
          show : true,
        lineWidth : 1,
        fill : true,
        fillColor : {
          colors : [{
            opacity : 0.1
          }, {
            opacity : 0.15
          }]
        }
        },
        points : {
          show : true
        },
        shadowSize : 0
      },
             xaxis : {
               mode : "time",
               tickLength : 10
             },

             yaxes : [{
               min : 20,
               tickLength : 5
             }],
             grid : {
               hoverable : true,
               clickable : true,
               tickColor : $chrt_border_color,
               borderWidth : 0,
               borderColor : $chrt_border_color,
             },
             tooltip : true,
             tooltipOpts : {
               content : "%s for <b>%x:00 hrs</b> was %y",
               dateFormat : "%y-%0m-%0d",
               defaultTheme : false
             },
             colors : [$chrt_main, $chrt_second],
             xaxis : {
               ticks : 15,
               tickDecimals : 2
             },
             yaxis : {
               ticks : 15,
               tickDecimals : 0
             },
    });

  }

  /* end site stats */

  /* updating chart */

  if ($('#updating-chart').length) {

    // For the demo we use generated data, but normally it would be coming from the server
    var data = [], totalPoints = 200;
    function getRandomData() {
      if (data.length > 0)
        data = data.slice(1);

      // do a random walk
      while (data.length < totalPoints) {
        var prev = data.length > 0 ? data[data.length - 1] : 50;
        var y = prev + Math.random() * 10 - 5;
        if (y < 0)
          y = 0;
        if (y > 100)
          y = 100;
        data.push(y);
      }

      // zip the generated y values with the x values
      var res = [];
      for (var i = 0; i < data.length; ++i)
        res.push([i, data[i]])
          return res;
    }

    // setup control widget
    var updateInterval = 1000;
    $("#updating-chart").val(updateInterval).change(function() {
      var v = $(this).val();
      if (v && !isNaN(+v)) {
        updateInterval = +v;
        if (updateInterval < 1)
      updateInterval = 1;
    if (updateInterval > 2000)
      updateInterval = 2000;
    $(this).val("" + updateInterval);
      }
    });

    // setup plot
    var options = {
      yaxis : {
        min : 0,
        max : 100
      },
      xaxis : {
        min : 0,
        max : 100
      },
      colors : [$chrt_fourth],
      series : {
        lines : {
          lineWidth : 1,
          fill : true,
          fillColor : {
            colors : [{
              opacity : 0.4
            }, {
              opacity : 0
            }]
          },
          steps : false

        }
      }
    };
    var plot = $.plot($("#updating-chart"), [getRandomData()], options);

    function update() {
      plot.setData([getRandomData()]);
      // since the axes don't change, we don't need to call plot.setupGrid()
      plot.draw();

      setTimeout(update, updateInterval);
    }

    update();

  }

  /*end updating chart*/

}

/* end flot charts */

/* ---------------------------------------------------------------------- */
/*	Sparklines setup
/* ---------------------------------------------------------------------- */	

function setup_sparklines(){

  if ($('.mystats').length){
    $('#balance').sparkline([11,8,40,40,18,40,33,15,42,25,10,20], {
      type : 'bar',
      barColor : $chrt_main,
      height : '30px',
      barWidth : "5px",
      barSpacing : "2px",
      zeroAxis : "false"
    });
    $('#clicks').sparkline([3,8,31,23,15,18,12,22,33,14,32,20], {
      type : 'bar',
      barColor : $chrt_second,
      height : '30px',
      barWidth : "5px",
      barSpacing : "2px",
      zeroAxis : "false"
    });
    $('#subscribe').sparkline([1,8,20,12,19,18,43,27,14,22,10,18], {
      type : 'bar',
      barColor : $chrt_third,
      height : '30px',
      barWidth : "5px",
      barSpacing : "2px",
      zeroAxis : "false"
    });
    $('#support').sparkline([18,17,22,19,23,18,22,24,17,20,16,17], {
      type : 'bar',
      barColor : $chrt_fourth,
      height : '30px',
      barWidth : "5px",
      barSpacing : "2px",
      zeroAxis : "false"
    });
  } // end if
}

/* end sparklines */

/* ---------------------------------------------------------------------- */
/*	Progress bar
/* ---------------------------------------------------------------------- */	

function progressbar_animate(){
  $('.progress .bar.filled-text').progressbar({
    display_text: 1,
  transition_delay: 1000,
  });

  $('.slim .bar').progressbar({
    transition_delay: 300
  });

  $('.delay .bar').progressbar({
    display_text: 1,
    transition_delay: 2000
  });

  $('.value .bar').progressbar({
    display_text: 1,
    use_percentage: false,
    transition_delay: 1000
  });

  $('.progress .bar.centered-text').progressbar({
    display_text: 2,
  });

  $('.progress .no-text').progressbar();
}

/* end progress bar */

/* ---------------------------------------------------------------------- */
/*	Toastr setup
/* ---------------------------------------------------------------------- */	

function setup_toastr() {

  toastr.options = {
    tapToDismiss : true,
    toastClass : 'toast',
    containerId : 'toast-container',
    debug : false,
    fadeIn : 250,
    fadeOut : 200,
    extendedTimeOut : 0,
    iconClasses : {
      error : 'toast-error',
      info : 'toast-info',
      success : 'toast-success',
      warning : 'toast-warning'
    },
    iconClass : 'toast-info',
    positionClass : 'toast-bottom-right',
    timeOut : 4500, // Set timeOut to 0 to make it sticky
    titleClass : 'toast-title',
    messageClass : 'toast-message'
  };

}

/* end toastr */

/* ---------------------------------------------------------------------- */
/*	Functions for idevice
/* ---------------------------------------------------------------------- */	

function execute_idevice_functions() {

  /* Function Detect iDevice 
     Documentation: http://ivaynberg.github.com/select2/	*/
  if((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i))) {

    /*	Initialize Hide iDevice Address bar */
    window.addEventListener("load",function() {			  
      setTimeout(function(){
        window.scrollTo(0, 1);  // Hide the address bar to increase user experience!
      }, 0);
    });			
    /*end hide address*/

  } else {
    // do nothing
    return false;
  }
  /* end if */
}

/* end functions for idevice*/


/* ---------------------------------------------------------------------- */
/*	All button functions
/* ---------------------------------------------------------------------- */	

function setup_all_buttons() {

  /* buttons */		
  $("#refresh-js").click(function() {
    toastr.warning('Please try again later', 'Database offline. No data available!');
    return false; 

  });

  $("#save-notes-btn-js").click(function() {
    toastr.success('Message have been saved to notes', 'Saved');
    return false; 
  });

  $("#post-btn-js").click(function() {
    toastr.error('Database is currently offline', 'Error');
    return false; 
  });

  /* end buttons */

  /* theme switcher */

  $('#theme-switcher ul#theme-links-js li a').bind('click',
      function(e) {
        $("#switch-theme-js").attr("href", "css/themes/"+$(this).data('rel')+".css");
        return false;
      }
      );

  /* end theme switcher */

  /* stop inbox tool bar dropdown from closing when clicked on a link */

  $('#theme-switcher ul.mailbox li a').bind('click',
      function(e) {
        return false;
      }
      );

  /* end inbox tool bar adjustment*/

  /* calendar buttons */

  $('div#calendar-buttons #btn-prev').click(function(){
    $('.fc-button-prev').click();
    return false;
  });

  $('div#calendar-buttons #btn-next').click(function(){
    $('.fc-button-next').click();
    return false; 
  });

  $('div#calendar-buttons #btn-today').click(function(){
    $('.fc-button-today').click();
    return false; 
  });

  $('div#calendar-buttons #btn-month').click(function(){
    $('#calendar').fullCalendar('changeView', 'month');
  });

  $('div#calendar-buttons #btn-agenda').click(function(){
    $('#calendar').fullCalendar('changeView', 'agendaWeek');
  });

  $('div#calendar-buttons #btn-day').click(function(){
    $('#calendar').fullCalendar('changeView', 'agendaDay');
  });

  /* end calendar buttons */

  /* inbox buttons */

  $('ul#mailbox-js > li > a').click(function(){
    show_inbox_menu_header();
  });

  $('#inbox-menu-header-js a.slashc-sliding-menu-home').click(function(){
    hide_inbox_menu_header();
  });

  /* end inbox buttons */

  /* logout button click */

  $('.logout-js').click(function(){
    $('body').addClass('logout');
    setTimeout(logout,400)
    return false; 
  });

  /* end logout button click */

  /* reset widget */
  $('a#reset-widget').click(function(){
    resetWidget();
    return false;
  });

  /* loading state button */

  $('#fat-btn').click(function() {
    var btn = $(this)
    btn.button('loading')
    setTimeout(function() {
      btn.button('reset')
    }, 3000)
  })

}

/* end all button functions */

/* ---------------------------------------------------------------------- */
/*	Logout
/* ---------------------------------------------------------------------- */

function logout(){

  var linky = $('.logout-js').data('rel');
  window.location.href = linky;

}

/* end logout */

/* ---------------------------------------------------------------------- */
/*	sound effects
/* ---------------------------------------------------------------------- */

function popsound() {
  //$pop_sound.play();
  $('embed').remove();
  $('body').append('<embed src="sounds/sound-pop-clear.mp3" autostart="true" hidden="true" loop="false">');
}

function play_sound_message_box(){
  //$messagebox.play(); //turn this on if your browser supports audio
}

function play_sound_big_box(){
  //$bigbox.play(); //turn this on if your browser supports audio
}

function play_sound_small_box(){
  //$smallbox.play(); //turn this on if your browser supports audio
}

/* sound effect */

/* ---------------------------------------------------------------------- */
/*	Slimscroll
/* ---------------------------------------------------------------------- */	

function setup_slimscroll(){

  /* mini inbox dropdown */
  $('ul#mailbox-slimscroll-js').slimScroll({
    height: '277px',
  width: '240px',
  disableFadeOut: true,
  distance: 3,
  size: 7
  });

  /* chat message box */
  $('div.chat-messages').slimScroll({
    height: '370px',
    disableFadeOut: true,
    railVisible:true, 
    distance: 3,
    size: 7
  });

  if ($('#inbox-menu-js').length){

    //$('h1#inbox-menu-header-js').slideUp(2200, 'easeOutSine');
    $('#inbox-menu-js').slimScroll({
      height: '518px',
      width: '249',
      disableFadeOut: true,
      distance: 3,
      size: 7
    });
    hide_inbox_menu_header()

      $('#inbox-loading-panel-js').slimScroll({
        height: '518px',
        width: 'auto',
        disableFadeOut: true,
        distance: 5,
        size: 7
      });


  }// end if

}

function hide_inbox_menu_header() {
  $('#inbox-menu-header-js').animate({"top" : "-42px"}, 250);
  $('#mailbox-js').animate({"top" : "-42px"}, 250);
}

function show_inbox_menu_header() {
  $('#inbox-menu-header-js').animate({"top" : "0px"}, 250);
  $('#mailbox-js').animate({"top" : "0px"}, 250);
}

/* end slimscroll */

/* ---------------------------------------------------------------------- */
/*	Easypie
/* ---------------------------------------------------------------------- */	

function setup_easypie(){

  /* lighter version */
  if ($('.percentage').length) { 
    $.percentage_easy_pie = $('.percentage');	
    $.percentage_easy_pie.easyPieChart({
      animate: 2000,
      trackColor:	"#515151",
      scaleColor:	"#515151",
      lineCap: 'butt',
      lineWidth: 20,
      barColor: function(percent) {
        percent /= 100;
        return "rgb(" + Math.round(255 * (1-percent)) + ", " + Math.round(255 * percent) + ", 0)";
      },
      size: 150
    });

  }// end if	

}

/* end easypie */

/* ---------------------------------------------------------------------- */
/*	Randomize easy pie
/* ---------------------------------------------------------------------- */		

function easypie_randomize(){

  var items = $.percentage_easy_pie;
  for (var i = 0; i < items.length; i++) {
    //do stuff
    var newValue = Math.round(100*Math.random());
    $(this).data('easyPieChart').update(newValue);
    $('span', this).text(newValue);
  } 
  //console.log(items.length);

}

/* end randomize */    	

/* ---------------------------------------------------------------------- */
/*	Chat message
/* ---------------------------------------------------------------------- */

function setup_wysihtml5() {

  if ($('#wysihtml5').length) {
    $('#wysihtml5').wysihtml5();
  }

}

/* end tooltips */

/* ---------------------------------------------------------------------- */
/*	Chat message
/* ---------------------------------------------------------------------- */

function setup_chatbox_demo() {

  /* message id */
  var id = 0;

  $.istying.focus(function() {
    $('.type-effect').show();
  });

  $.istying.blur(function() {
    $('.type-effect').hide();
  });

  /* on button press */
  $('#send-msg-js').click(function() {
    var msg_input = $.istying.val();
    if (msg_input.length) {
      var msg_input = $.istying.val();
      id++;
      $('.tab-pane.active > div > .chat-messages').prepend('<p id="message-dynamic-' + id + '" class="message-box you"><img src="img/avatar/avatar_0.jpg" alt=""><span class="message"><strong>Me</strong><span class="message-time">by Victoria at 14:25pm, 4th Jan 2013</span><span class="message-text">' + msg_input + '</span></span></p>')
    $('.tab-pane.active > div > .chat-messages #message-dynamic-' + id).hide().fadeIn(750);
  //console.log(msg_input.trim() + id);
  $.istying.val('');
  play_sound_small_box();
    }
    return false; 

  });

  /* on key press enter */
  $.istying.on('keyup', function(e) {

    if (e.keyCode == 13) {
      var msg_input = $.istying.val();
      if (msg_input.length) {
        var msg_input = $.istying.val();
        id++;
        $('.tab-pane.active > div > .chat-messages').prepend('<p id="message-dynamic-' + id + '" class="message-box you"><img src="img/avatar/avatar_0.jpg" alt=""><span class="message"><strong>Me</strong><span class="message-time">by Victoria at 14:25pm, 4th Jan 2013</span><span class="message-text">' + msg_input + '</span></span></p>')
    $('.tab-pane.active > div > .chat-messages #message-dynamic-' + id).hide().fadeIn(750);
  //console.log(msg_input.trim() + id);
  $.istying.val('');
  play_sound_small_box();
      }
    }// end if
  });

}

/* end chat message */

/* ---------------------------------------------------------------------- */
/*	Bootbox
/* ---------------------------------------------------------------------- */	

function setup_bootbox_demo() {
  if ($('ul#bootbox-js').length){

    $('ul#bootbox-js a#bootbox-basic-js').click(function(e) {
      e.preventDefault();
      play_sound_message_box();
      bootbox.alert("Hello world!", function() {
        //console.log("Hello world callback");
      });
    });

    $('ul#bootbox-js a#bootbox-confirm-js').click(function(e) {
      e.preventDefault();
      play_sound_message_box();
      bootbox.confirm("Are you sure?", function(result) {
        //console.log("Confirm result: "+result);
        toastr.info("Confirm result: "+result);
      });
    });

    $('ul#bootbox-js a#bootbox-prompt-js').click(function(e) {
      e.preventDefault();
      play_sound_message_box();
      bootbox.prompt("What is your favourite website?", "None!", "Alright!", function(result) {
        //console.log(result);
        toastr.info('You have picked '+result)
      }, "wrapbootstrap.com");
    }); 

    $('ul#bootbox-js a#bootbox-cust-js').click(function(e) {
      e.preventDefault();
      play_sound_message_box();
      bootbox.dialog("I am a custom dialog", [{
        "label" : "Success!",
        "class" : "btn-success medium",
        "callback": function() {
          //console.log("great success");
          toastr.success("Great Success!");
        }
      }, {
        "label" : "Danger!",
        "class" : "btn-danger medium",
        "callback": function() {
          //console.log("uh oh, look out!");
          toastr.error("uh oh, look out!");
        }
      }, {
        "label" : "Click ME!",
        "class" : "btn-primary medium",
        "callback": function() {
          //console.log("Primary button");
          toastr.info("You clicked the blue button :)");
        }
      }]);
    });

    $("ul#bootbox-js a#bootbox-icon-js").click(function(e) {
      e.preventDefault();
      play_sound_message_box();
      bootbox.dialog("Custom dialog with icons passed into <b>bootbox.dialog</b>.", [{
        "label" : "Success!",
        "class" : "btn-success medium",
        "icon"  : "cus-bell",
        "callback": function() {
          //console.log("great success");
          toastr.success("Great Success!");
        }
      }, {
        "label" : "Danger!",
        "class" : "btn-danger medium",
        "icon"  : "cus-delete",
        "callback": function() {
          //console.log("uh oh, look out!");
          toastr.error("uh oh, look out!");
        }
      }, {
        "label" : "Click ME!",
        "class" : "btn-primary medium",
        "icon"  : "cus-cursor",
        "callback": function() {
          //console.log("Primary button");
          toastr.info("You clicked the blue button :)");
        }
      }, {
        "label" : "Just a button...",
        "icon"  : "cus-image-2",
        "callback": function() {
          //console.log("Primary button");
          toastr.warning("Just a button...");
        }
      }]);
    });

  }// end if
}

/* ---------------------------------------------------------------------- */
/*	Enable Select2
/* ---------------------------------------------------------------------- */

function setup_custom_form_elements() {
  if ($('.themed').length) {
    $(".themed input[type='radio'], .themed input[type='checkbox'], .themed input[type='file'].file, .themed textarea").uniform();
    $(".themed select.with-search").select2();

    /* some demo buttons for select 2 */

    $("#disable-select-demo").click(function() {
      $("#select-demo-js select").select2("disable");
    });

    $("#enable-select-demo").click(function() {
      $("#select-demo-js select.with-search").select2();
    }); 

  }// end if
}

/* end select2 */

/* ---------------------------------------------------------------------- */
/*	Setup_datepicker_demo
/* ---------------------------------------------------------------------- */	

function setup_datepicker_demo() {
  if ($('#datepicker-js').length){
    $('#datepicker-js, #datepicker-js-2').datepicker()
  }// end if
}	

/* end setup_datepicker_demo */

/* ---------------------------------------------------------------------- */
/*	Setup_colorpicker_demo
/* ---------------------------------------------------------------------- */	

function setup_colorpicker_demo() {
  if ($('#colorpicker-js').length){
    $('#colorpicker-js, #colorpicker-js-2, #colorpicker-js-3').colorpicker()
  }// end if
}	

/* end setup_datepicker_demo */

/* ---------------------------------------------------------------------- */
/*	Setup_masked_input
/* ---------------------------------------------------------------------- */	

function setup_masked_input() {
  if ($('#masked-inputs-js').length){

    $.mask.definitions['~'] = "[+-]";
    $(".date-masked").mask("99/99/9999", {
      completed : function() {
        toastr.success('Date entry was correct!', 'Correct Date');
      }
    });
    $(".phone-masked").mask("(999) 999-9999");
    $(".ssn-masked").mask("999-99-9999");
    $(".productkey-masked").mask("a*-999-a999", {
      placeholder : " "
    });
    $(".purchase-order-masked").mask("PO: aaa-999-***"); 
    //console.log("masked input fired!")
  }// end if
}	

/* end setup_masked_input */

/* ---------------------------------------------------------------------- */
/*	Setup_timepicker
/* ---------------------------------------------------------------------- */	

//documentation: http://jdewit.github.com/bootstrap-timepicker/index.html

function setup_timepicker() {
  if ($('#timepicker-demo').length) {

    /* default */
    $('#timepicker1').timepicker();

    /* in model */
    $('#timepicker2').timepicker({
      minuteStep: 1,
      template: 'modal',
      showSeconds: true,
      showMeridian: false
    });
  }
}

/* end setup_timepicker */

/* ---------------------------------------------------------------------- */
/*	Setup_uislider
/* ---------------------------------------------------------------------- */	

//reference: https://groups.google.com/forum/?fromgroups=#!topic/twitter-bootstrap-stackoverflow/ko8GIGczZ54

function setup_uislider() {
  if ($('#uislider-demo').length) {	

    $("#slider-range").slider({
      range: true,
    min: 100,
    max: 500,
    values: [176, 329],
    slide: function(event, ui) {
      $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);

      $('#slider-range .ui-slider-handle:first').html('<div class="tooltip top slider-tip"><div class="tooltip-arrow"></div><div class="tooltip-inner">' + ui.values[0] + '</div></div>');
      $('#slider-range .ui-slider-handle:last').html('<div class="tooltip top slider-tip"><div class="tooltip-arrow"></div><div class="tooltip-inner">' + ui.values[1] + '</div></div>');
    }
    });
    $("#amount").val("$" + $("#slider-range").slider("values", 0) + " - $" + $("#slider-range").slider("values", 1));


    $( "#slider-range-min" ).slider({
      range: "min",
      value: 461,
      min: 100,
      max: 900,
      slide: function( event, ui ) {
        $( "#amount2" ).val( "$" + ui.value );
        $('#slider-range-min .ui-slider-handle:first').html('<div class="tooltip top slider-tip"><div class="tooltip-arrow"></div><div class="tooltip-inner">' + ui.value + '</div></div>');
      }
    });
    $("#amount2").val( "$" + $( "#slider-range-min" ).slider("value"));


    $( "#slider-range-max" ).slider({
      range: "max",
      min: 100,
      max: 999,
      value: 507,
      slide: function( event, ui ) {
        $( "#amount3" ).val( "$" + ui.value );
        $('#slider-range-max .ui-slider-handle:first').html('<div class="tooltip top slider-tip"><div class="tooltip-arrow"></div><div class="tooltip-inner">' + ui.value + '</div></div>');
      }
    });
    $("#amount3" ).val( "$" + $( "#slider-range-max" ).slider( "value" ));

    $("#slider-range-step").slider({
      range: true,
      min: 100,
      max: 999,
      step:100,
      values: [250, 850],
      slide: function(event, ui) {
        $("#amount4").val("$" + ui.values[0] + " - $" + ui.values[1]);

        $('#slider-range-step .ui-slider-handle:first').html('<div class="tooltip top slider-tip"><div class="tooltip-arrow"></div><div class="tooltip-inner">' + ui.values[0] + '</div></div>');
        $('#slider-range-step .ui-slider-handle:last').html('<div class="tooltip top slider-tip"><div class="tooltip-arrow"></div><div class="tooltip-inner">' + ui.values[1] + '</div></div>');
      }
    });
    $("#amount4").val("$" + $("#slider-range-step").slider("values", 0) + " - $" + $("#slider-range-step").slider("values", 1));

  }
}

/* end setup_uislider */

/* ---------------------------------------------------------------------- */
/*	Validation_setup_demo
/* ---------------------------------------------------------------------- */

//documentation: http://docs.jquery.com/Plugins/Validation/

function validation_setup_demo() {
  if ($('#validate-demo-js').length) {
    $("#validate-demo-js").validate({
      rules : {
        simple : "required",
      minString : {
        required : true,
      minlength : 3
      },
      maxString : {
        required : true,
      maxlength : 5
      },
      minNumber : {
        required : true,
      min : 3
      },
      maxNumber : {
        required : true,
      max : 5
      },
      rangeValue : {
        required : true,
        range : [5, 10]
      },
      emailValidation : {
        required : true,
        email : true
      },
      urlValidation : {
        required : true,
        url : true
      },
      dateValidation : {
        required : true,
        date : true
      },
      noStrings : {
        required : true,
        digits : true
      },
      password : {
        required : true,
        minlength : 5
      },
      passwordRepeat : {
        required : true,
        minlength : 5,
        equalTo : "#password"
      },
      topic : {
        required : "#newsletter:checked",
        minlength : 2
      },
      agree : "required"
      }, // end rules
            highlight : function(label) {
              $(label).closest('.control-group').removeClass('success');
              $(label).closest('.control-group').addClass('error');
            },
            success : function(label) {
              label.text('').addClass('valid').closest('.control-group').addClass('success');
            }
    });
  }// end if

} 

/* end validation_setup_demo */

/* ---------------------------------------------------------------------- */
/*	Setup_wizard_demo
/* ---------------------------------------------------------------------- */	

function setup_wizard_demo() {
  if ($('#wizard_name').length) {
    $('#wizard_name').bootstrapWizard({
      'tabClass' : 'nav',
      'debug' : false,
      onShow : function(tab, navigation, index) {
        //console.log('onShow');
      },
      onNext : function(tab, navigation, index) {
        //console.log('onNext');
        if (index == 1) {
          // Make sure we entered the name
          if (!$('#name').val()) {
            //alert('You must enter your name');
            $('#name').focus();
            $('#name').closest('.control-group').removeClass('success');
            $('#name').closest('.control-group').addClass('error');
            return false;
          }
          if (!$('#lname').val()) {
            //alert('You must enter your last name');
            $('#lname').focus();
            $('#lname').closest('.control-group').removeClass('success');
            $('#lname').closest('.control-group').addClass('error');
            return false;
          }
        }
        /*$.jGrowl("Its nice to finally meet you! Please remember <b>"+$('#name').val()+",</b> this is only a demo. Not all the functions will work. For full documentation please see the link on top of the page", { 
          header: 'Hey there ' + $('#name').val()+'!', 
          sticky: true,
          theme: 'with-icon',
          easing: 'easeOutBack',
          animateOpen: { 
          height: "show"
          },
          animateClose: { 
          opacity: 'hide' 
          }
          });*/	
        // Set the name for the next tab
        //$('#inverse-tab3').html('Hello, ' + $('#name').val());

      },
             onPrevious : function(tab, navigation, index) {
               //console.log('onPrevious');
             },
             onLast : function(tab, navigation, index) {
               //console.log('onLast');
             },
             onTabClick : function(tab, navigation, index) {
               //console.log('onTabClick');
               alert('on tab click disabled');
               return false;
             },
             onTabShow : function(tab, navigation, index) {
               //console.log('onTabShow');
               var $total = navigation.find('li').length;
               var $current = index + 1;
               var $percent = ($current / $total) * 100;
               $('#wizard_name').find('.bar').css({
                 width : $percent + '%'
               });
             }
    });
  }// end if

}

/* end setup_wizard_demo */

/* ---------------------------------------------------------------------- */
/*	Setup checkedin tables
/* ---------------------------------------------------------------------- */

function setup_checkedin_tables_demo() {

  if ($("table.checked-in").length){
    $("td input[type='checkbox']").click(function(){
      if ($(this).is(':checked')){
        $(this).parent().addClass("highlighted");
        $(this).parent().siblings().addClass("highlighted");
      } else if($(this).parent().is(".highlighted")) {
        $(this).parent().removeClass("highlighted");
        $(this).parent().siblings().removeClass("highlighted");
      }
    });
  }// end if

}

/* end checkedin tables */

/* ---------------------------------------------------------------------- */
/*	Activate_bt_accordion_hack
/* ---------------------------------------------------------------------- */	

$(function() {

  // credit: http://stackoverflow.com/questions/10918801/twitter-bootstrap-adding-a-class-to-the-open-accordion-title
  $('.accordion').on('show', function (e) {
    $(e.target).prev('.accordion-heading').find('.accordion-toggle').addClass('active');
  });

  $('.accordion').on('hide', function (e) {
    $(this).find('.accordion-toggle').not($(e.target)).removeClass('active');
  });

});

/* end activate_bt_accordion_hack */

/* ---------------------------------------------------------------------- */
/*	Window.resize functions
/* ---------------------------------------------------------------------- */	

$(window).resize(function(){


});

/* end window.resize functions */

/* ---------------------------------------------------------------------- */
/*	Window.load functions
/* ---------------------------------------------------------------------- */	

$(window).load(function(){


});

/* end window.load functions */
