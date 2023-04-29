function b12(num) {
  b12for = document.querySelector(`.b12for${num}`);
  allb12for = document.querySelectorAll(".bb21");
  var div_arrayfb12for = [...allb12for]; // converts NodeList to Array
  div_arrayfb12for.forEach((div) => {
    if (div.className == `bb21 b12for${num} cb${num}`) {
      div.style.display = "flex";
    }
    else if (div.className == `bb21 b12for${num} cb${num} big_bb21`) {
      div.style.display = "flex";
    }
    else {
      div.style.display = "none";
    }
  });
}

$("#dropdownID").hide();

$(document).ready(function () {
  $("#nav_serc").keypress(function () {
    $("#dropdownID").show();
    $.ajax({
      type: "POST",
      url: "search.php",
      data: {
        name: $("#nav_serc").val(),
        typ: "nav",
        sity: "0",
      },
      success: function (data) {
        $("#nav_output").html(data);
      },
    });
    $.ajax({
      type: "POST",
      url: "search.php",
      data: {
        name: $("#nav_serc").val(),
        typ: "nav_kays",
        sity: "0",
      },
      success: function (data) {
        $("#nav_output4").html(data);
      },
    });
    $.ajax({
      type: "POST",
      url: "search.php",
      data: {
        name: $("#nav_serc").val(),
        typ: "nav_pr",
        sity: "0",
      },
      success: function (data) {
        $("#nav_output2").html(data);
      },
    });
  });
  $("#nav_serc").keyup(function () {
    $("#dropdownID").show();
    $.ajax({
      type: "POST",
      url: "search.php",
      data: {
        name: $("#nav_serc").val(),
        typ: "nav",
        sity: "0",
      },
      success: function (data) {
        $("#nav_output").html(data);
      },
    });
    $.ajax({
      type: "POST",
      url: "search.php",
      data: {
        name: $("#nav_serc").val(),
        typ: "nav_kays",
        sity: "0",
      },
      success: function (data) {
        $("#nav_output4").html(data);
      },
    });
    $.ajax({
      type: "POST",
      url: "search.php",
      data: {
        name: $("#nav_serc").val(),
        typ: "nav_pr",
        sity: "0",
      },
      success: function (data) {
        $("#nav_output2").html(data);
      },
    });
  });
});

$(document).click(function (e) {
  if ($(e.target).closest("#dropdownID").length != 0) return false;
  $("#dropdownID").hide();
});

function hide() {
  [...document.querySelectorAll(`.bb21`)].forEach((div) => {
    div.style.display = "none";
  });
}

[...document.querySelectorAll(`.bb21`)].forEach((mdsad) => {
  if(mdsad.querySelector('.dwad').children.length > 8){
    mdsad.classList.add("big_bb21");
    mdsad.querySelector('.sadow').classList.add("sm_sadow");
  }
});

function cat() {
  e = document.getElementById("category");
  z = document.getElementById("nav-menu");
  c = document.getElementById("chang");
  src = c.getAttribute("data-original");
  src_change = c.getAttribute("data-orchangeiginal");

  if (e.style.display == "none") {
    z.style.height = 85 + "%";
    z.style.alignContent = "space-between";
    e.style.display = "flex";
    // c.src = "{% static 'img/icons/down-arrow.png' %}";
    c.setAttribute("src", src_change);
  } else {
    z.style.height = 4 + "rem";
    e.style.display = "none";
    c.setAttribute("src", src);
  }
}

function lchanf(num) {
  catfor = document.querySelector(`.catfor${num}`);
  allcatfor = document.querySelectorAll(".cf");
  var div_array = [...allcatfor]; // converts NodeList to Array
  div_array.forEach((div) => {
    if (div.className == `cf catfor${num}`) {
      div.style.display = "flex";



    } else {
      div.style.display = "none";
    }

  });


}
el = document.querySelectorAll(".cat");
for (let i = 0; i < el.length; i++) {
  el[i].onmouseover = function () {
    var c = 0;
    while (c < el.length) {
      el[c++].className = "cat";
    }

    el[i].className = "cat actcat";
  };
}

function imgSlider(anything) {
  if (document.querySelector(".det .imgs .gmi img").src != anything) {
    document.querySelector(".det .imgs .gmi img").src = anything;
  }
}
iasd = document.querySelectorAll(".det .imgs .imges .img");
for (let m = 0; m < iasd.length; m++) {
  iasd[m].onmouseover = function () {
    var l = 0;
    while (l < iasd.length) {
      iasd[l++].className = "img";
    }

    iasd[m].className = "img activeimg";
  };
}
