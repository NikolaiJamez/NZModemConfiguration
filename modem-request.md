---
layout: page
title: Modem Request Form
---
<script>
  window.addEventListener("load", function() {
    const form = document.getElementById('modem-request-form');
    form.addEventListener("submit", function(e) {
      e.preventDefault();
      const data = new FormData(form);
      const action = e.target.action;
      fetch(action, {
        method: 'POST',
        body: data,
      })
      .then(() => {
        alert("Success!");
      })
    });
  });
</script>
<form
  id="modem-request-form"
  method="POST" 
  action="https://script.google.com/macros/s/AKfycbzVC9BO2BItSWnA5n7aEd3HH2x2GE-ikkwNgP8zHAy4CI19_GGj4lbA5ZzuQkF3LWDN/exec"
>
  <input label="Your name"name="Name" type="test" placeholder="Your name" required>
  <input label="Modem Make"name="Make" type="text" placeholder="e.g. TP Link, ASUS, etc..." required>
  <input label="Modem Model"name="Model" type="text" placeholder="e.g. Deco X55, etc..." required>
  <input name="Completed" type="hidden" value="FALSE" required>
  <button type="submit">Send</button>
</form>
