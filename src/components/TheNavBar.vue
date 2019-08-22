<template lang="pug">
  b-navbar(toggleable="sm"
      type="dark"
      variant="dark"
      align="center"
      sticky)
    b-navbar-brand
    b-navbar-toggle(target="nav-collapse")
    b-collapse#nav-collapse(is-nav)
      b-navbar-nav.w-100(fill)
          b-nav-item(to="/") Home
          b-nav-item(to="/") Skills
          b-nav-item(to="/") About
          b-nav-item(to="/") Contact
</template>

<script>
export default {
  name: "TheNavBar"
};
</script>
