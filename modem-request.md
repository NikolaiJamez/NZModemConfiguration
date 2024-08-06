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
  action="https://script.google.com/macros/s/AKfycbzVC9BO2BItSWnA5n7aEd3HH2x2GE-ikkwNgP8zHAy4CI19_GGj4lbA5ZzuQkF3LWDN/exec">
  <div class="form-group">
    <label for="name">Your Name</label>
    <input name="Name" type="text" class="form-control" id="Name" aria-describedby="nameHelp" placeholder="Enter your name">
    <small id="nameHelp" class="form-text text-muted">Just your first name is fine</small>
  </div>
  <div class="form-group">
    <label for="Make">Modem Make</label>
    <input name="Make" type="text" class="form-control" id="Make" aria-describedby="makeHelp" placeholder="E.g. TP Link, ASUS, Netgear, etc...">
    <small id="makeHelp" class="form-text text-muted">The Make or Brand of the modem</small>
  </div>
  <div class="form-group">
    <label for="Model">Modem Model</label>
    <input name="Model" type="text" class="form-control" id="Model" aria-describedby="modelHelp" placeholder="E.g. Dexo X55, RAX10, etc...">
    <small id="modelHelp" class="form-text text-muted">The Model of the modem</small>
  </div>
  <button type="submit" class="btn btn-secondary">Submit</button>
</form>
