<template lang="pug">
  b-navbar(toggleable="sm"
      type="dark"
      variant="dark"
      align="center"
      fixed="bottom"
      v-b-scrollspy)
    b-navbar-brand
    b-navbar-toggle(target="nav-collapse")
    b-collapse#nav-collapse(is-nav)
      b-navbar-nav.w-100(fill)
          b-nav-item(href="#home") Home
          b-nav-item(href="#skills") Skills
          b-nav-item(href="#about") About
          b-nav-item(href="#contact") Contact
</template>

<script>
export default {
  name: "TheNavBar"
};
</script>

<style scoped>
  .bg-dark {
    background-color: #141a20 !important
  }
</style>
