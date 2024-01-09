() => {
  var bodyElement = document.querySelector("body");
  if (bodyElement) {
    var computedStyle = window.getComputedStyle(bodyElement);
    var fontFamily = computedStyle.getPropertyValue("font-family");
    return fontFamily;
  } else {
    return "Element not found";
  }
};
