<template lang="pug">
  b-navbar(toggleable="sm"
      type="dark"
      variant="dark"
      align="center"
      fixed="bottom"
      v-b-scrollspy:nav-scroller)
    b-navbar-brand
    b-navbar-toggle(target="nav-collapse")
    b-collapse#nav-collapse(is-nav)
      b-navbar-nav.w-100(fill)
          b-nav-item(href="#home" @click="scrollIntoView") Home
          b-nav-item(href="#skills" @click="scrollIntoView") Skills
          b-nav-item(href="#about" @click="scrollIntoView") About
          b-nav-item(href="#contact" @click="scrollIntoView") Contact
</template>

<script>
export default {
  name: "TheNavBar"
};
</script>
