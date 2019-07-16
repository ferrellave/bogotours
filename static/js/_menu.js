
<script type="text/javascript">
    function menutours(){
       var menutours = document.getElementById("menutours")
       if(menutours.className=='menutours-close'){
        menutours.className='menutours-open'
       } else{
        menutours.className='menutours-close'
       }
    }
        movelogo();
    function move(){
        setTimeout(function(){ 
            document.getElementById("backing").className = "backing2";
         },4000);
    }

    function movelogo(){
        setTimeout(function(){ 
            document.getElementById("icon").className = "icon2";
         },4000);
    }

window.onscroll = function() {
  windowScroll();
};

function windowScroll() {
    var mainNav = document.getElementById('menu-lefts');
  if (document.body.scrollTop > 140 || document.documentElement.scrollTop > 140) {
    mainNav.className = "menu-left-scroll";
  } else {
    mainNav.className = "menu-left";
  }
}
</script>