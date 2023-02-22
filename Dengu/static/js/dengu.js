// start the owl process

$(document).ready(function () {
  $(".owl-carousel").owlCarousel();
  $('.carousel').carousel({pause: 'none'})
  $('#myModal').modal("show");
  $('#myModal').modal("hide");
  $('#myModal').modal("toggle");
});

// changes the website background color to selected season
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

const season = {
  January: "rgba(89,157,201,0.7) 0%, rgba(18,99,152,1) 100%",
  February: "rgba(89,157,201,0.7) 0%, rgba(18,99,152,1) 100%",
  March: "rgba(249,245,134,0.7) 0%, rgba(150,251,196,1) 100%",
  April: "rgba(249,245,134,0.7) 0%, rgba(150,251,196,1) 100%",
  May: "rgba(249,245,134,0.7) 0%, rgba(150,251,196,1) 100%",
  June: "rgba(209,253,255,0.7) 0%, rgba(253,219,146,1) 100%",
  July: "rgba(209,253,255,0.7) 0%, rgba(253,219,146,1) 100%",
  August: "rgba(209,253,255,0.7) 0%, rgba(253,219,146,1) 100%",
  September: "rgba(249,212,35,0.7) 0%, rgba(200,85,52,1) 100%",
  October: "rgba(249,212,35,0.7) 0%, rgba(200,85,52,1) 100%",
  November: "rgba(249,212,35,0.7) 0%, rgba(200,85,52,1) 100%",
  December: "rgba(89,157,201,0.7) 0%, rgba(18,99,152,1) 100%",
};


const d = new Date();
let month = months[d.getMonth()];

const seasons = {
  SPRING: "rgba(249,245,134,0.7) 0%, rgba(92,201,85,1) 100%",
  SUMMER: "rgba(209,253,255,0.7) 0%, rgba(253,219,146,1) 100%",
  AUTUMN: "rgba(249,212,35,0.7) 0%, rgba(200,85,52,1) 100%",
  WINTER: "rgba(89,157,201,0.7) 0%, rgba(18,99,152,1) 100%",
};

const category_color = {
  SPRING: "#0c79ac",
  SUMMER: "#67d80a",
  AUTUMN: "#910000",
  WINTER: "#7d11d4",
};

// var text_colors = document.querySelectorAll(".card-title, .topmenuItem, .dropdown-item, .nav-link");
var text_colors = document.querySelectorAll(".dropdown-item, .dropdown-menu");
var text_colors2 = document.querySelectorAll(".dropdown-item");
var category_title = document.querySelectorAll(".categoryCard h5");
var cart_items = document.querySelectorAll(".cart-items");
var cart_item_season = document.querySelectorAll(".cart-item-season");

current_season = document.getElementById("currentSeason").innerHTML;

var path = window.location.pathname.split("/");
  if (path[2] == 'SPRING' || path[2] == 'SUMMER' || path[2] == 'AUTUMN' || path[2] == 'WINTER'){
    current_season = path[2]
    console.log(path)
  }
document.getElementById("currentSeason").style.display = "none";


function seasonChange(navImage = season[month]) {
  // document.body.style.background = "background: rgb(217,74,4);";
  document.body.style.backgroundImage = `linear-gradient(to top, ${navImage})`;
  document.body.style.backgroundRepeat = "no-repeat";
  document.body.style.backgroundAttachment = "fixed";
  document.body.style.backgroundSize = "cover";
  // console.log("this is the color", navImage.split("0%,", 2).pop().slice(0, -5));
  document.getElementById("navbar1").style.backgroundImage = `linear-gradient(to top, ${navImage})`;
  document.getElementById("searchBar").style.backgroundImage = `linear-gradient(to top, ${navImage})`;
  document.getElementById("searchBar").style.color = `black`;
  
  for (var i = 0; i < text_colors.length; i++) {
    text_colors[i].style.backgroundColor = `${navImage.slice(0, 20)}`;
  }
  text_colors2.forEach((text) => {
    text.addEventListener("mouseover", function handleClick(event) {
      text.setAttribute("style", `background-color: ${navImage.split("0%,", 2).pop().slice(0, -5)};`);
    });
    text.addEventListener("mouseout", function handleClick(event) {
      text.setAttribute("style", `background-color: ${navImage.split("0%,", 4)};`);
    });
  });
  try {
    for (i = 0; i < category_title.length; i++) {
      category_title[i].style.color = `${category_color[current_season]}`;
    }
    for (i = 0; i < cart_items.length; i++) {
      // cart_items[i].style.boxShadow = `-9px 0 15px 0px ${seasons[cart_item_season[i].innerHTML.split(",", 1)].split("0%,")[1].slice(0, -5)}`
      cart_items[i].style.border = `3px solid ${seasons[cart_item_season[i].innerHTML.split(",", 1)].split("0%,")[1].slice(0, -5)}`
      console.log(seasons[cart_item_season[i].innerHTML.split(",", 1)].split("0%,")[1].slice(0, -5))
    }

    // document.getElementById("cartid").style.backgroundImage = `linear-gradient(to bottom, ${navImage})`;
  } catch {}
}

seasonChange(seasons[current_season]);

// function seasonColor(color){
//   document.getElementById("currentSeason").innerHTML = color
//   console.log(color)
// }


// function textColor(txtColor = seasons_color[month]){
//   for (var i = 0; i < text_colors.length; i++) {
//     text_colors[i].style.color = txtColor}
// }

// textColor(seasons_color[current_season])

// adds items to the cart

var updateBtn = document.getElementsByClassName("update-cart");
for (var i = 0; i < updateBtn.length; i++) {
  updateBtn[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("user:", user);
    console.log("productId:", productId, "action:", action);

    if (user === "AnonymousUser") {
      console.log("not logged in");
    } else {
      console.log("user is logged in");
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  var url = "/update_item";
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      document.getElementById("cartCount").innerHTML = data[0];
      if (data[2] === 0) {
        location.reload();
      }
      try {
        document.getElementById("cartTotal").innerHTML = data[0];
        document.getElementById("cartSum").innerHTML = data[1];
        document.getElementById(productId).innerHTML = data[2];
        document.getElementById(`${productId}SUM`).innerHTML = `$${data[3]}`;
      } catch (TypeError) {}
    });
}

// function to separate the credit card number/////////////////////////////////////////////////////////////////////
function regexCCnumber() {
  try {
    var CCnumber = document.getElementById("CCnumber").value.split(" ").join("");
    document.getElementById("CCnumber").value = CCnumber.match(/.{1,4}/g).join(" ");
  } catch (TypeError) {}
}

var cartform = document.getElementById("cartForm");

// try {
//   cartform.addEventListener("submit", function (e) {
//     e.preventDefault();
//     console.log("form prevented successfully");
//   });
//   document.getElementById("checkoutButton").addEventListener("click", function (e) {
//     submitCheckout();
//   });
// } catch (TypeError) {}

function submitCheckout() {
  console.log("order completed");
  var id_list = [];
  var allID = document.getElementsByClassName("product_id");
  for (var i = 0; i < allID.length; i++) {
    id_list.push(allID[i].dataset.product);
  }

  var shippingInfo = {
    first_name: cartform.SHIPname.value,
    last_name: cartform.SHIPlast.value,
    phone: cartform.SHIPphone.value,
    email: cartform.SHIPemail.value,
    country: cartform.SHIPcountry.value,
    city: cartform.SHIPcity.value,
    street: cartform.SHIPstreet.value,
    zip: cartform.SHIPzip.value,
    total: document.getElementById("cartSum").innerHTML,
  };
  console.log(shippingInfo["total"]);
  var url = "/complete";
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify({ shippingInfo: shippingInfo, id_list: id_list }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      alert("Order completed successfully");
      window.location.href = "/";
    });
}

// function openTab(evt, cityName) {
//   var i, tabcontent, tablinks;
//   tabcontent = document.getElementsByClassName("tabcontent");
//   for (i = 0; i < tabcontent.length; i++) {
//     tabcontent[i].style.display = "none";
//   }
//   tablinks = document.getElementsByClassName("tablinks");
//   for (i = 0; i < tablinks.length; i++) {
//     tablinks[i].className = tablinks[i].className.replace(" active", "");
//   }
//   document.getElementById(cityName).style.display = "block";
//   evt.currentTarget.className += " active";
// }

// document.getElementById("defaultOpen").click();

// function regexCCdate() {
//   try {
//     var CCnumber = document.getElementById("CCdate").value.split("/").join("");
//     document.getElementById("CCdate").value = CCnumber.match(/.{1,2}/g).join("/");
//   } catch (TypeError) {}
// }

// function seasonChange(navImage) {
//   if (sessionStorage.getItem("colour")) {
//     document.body.style.background = "background: rgb(217,74,4);";
//     document.body.style.backgroundImage = `linear-gradient(to top, ${navImage})`;
//     document.body.style.backgroundRepeat = "no-repeat";
//     document.body.style.backgroundAttachment = "fixed";
//     document.body.style.backgroundSize = "cover";
//     document.getElementById(
//       "navbar1"
//     ).style.backgroundImage = `linear-gradient(to top, ${navImage})`;
//   } else {
//     document.body.style.background = "background: rgb(217,74,4);";
//     document.body.style.backgroundImage = `linear-gradient(to top, ${navImage})`;
//     document.body.style.backgroundRepeat = "no-repeat";
//     document.body.style.backgroundAttachment = "fixed";
//     document.body.style.backgroundSize = "cover";
//     document.getElementById(
//       "navbar1"
//     ).style.backgroundImage = `linear-gradient(to top, ${navImage})`;
//   }
// }

// seasonChange(season[month]);

// function photosChange(seasonImg) {
//   var originalImage = document.getElementsByClassName("seasonChangeImg");
//   console.log(originalImage);
//   for (let i = 0; i < originalImage.length; i++) {
//     originalImage[
//       i
//     ].src = `../../static/media/season slideshow/${seasonImg}/${seasonImg}${i}.jpg`;
//   }
// }
