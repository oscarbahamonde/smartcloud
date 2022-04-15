function dqs(selector) {
    return document.querySelector(selector);
}

function dqsa(selector) {
    return document.querySelectorAll(selector);
}

function dgebi(id) {
    return document.getElementById(id);
}

function dael(element, event, callback) {
    element.addEventListener(event, callback);
}

function newEl(tag) {
    return document.createElement(tag);
}

function appEl(parent, child) {
    parent.appendChild(child);
}

function delEl(element) {
    return element.remove();
}

function getText(element) {
    return element.textContent;
}

function setText(element, text) {
    element.innerText = text;
}

function setHTML(element, html) {
    element.innerHTML = html;
}

function setAttr(element, attribute, value) {
    element.setAttribute(attribute, value);
}

function addClass(element, className) {
    element.classList.add(className);
}

function removeClass(element, className) {
    element.classList.remove(className);
}

function toggleClass(element, className) {
    element.classList.toggle(className);
}

export default {
    dqs,
    dqsa,
    dgebi,
    dael,
    newEl,
    appEl,
    delEl,
    getText,
    setText,
    setHTML,
    setAttr,
    addClass,
    removeClass,
    toggleClass
};
