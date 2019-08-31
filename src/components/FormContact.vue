<template lang="pug">
    b-form#contact-form(

        action="https://formspree.io/IrvinJohnathan@gmail.com",
        method="post"
    )
        b-form-group(
            id="contact-group-1",
            label="Email Address:",
            label-for="contact-input-1",
            name="simple-contact-form",
            description="By submitting your email, you agree to join our mailing list."
        )
            b-form-input(
                id="contact-input-1",
                v-model="form.email",
                type="email",
                placeholder="example@example.com",
                name="_replyto",
                required
            )
        b-form-group(
            id="contact-group-2",
            label="Your Name:",
            label-for="contact-input-2",
            description="Profanity, and spam are filtered."
        )
            b-form-input(
                id="contact-input-2",
                v-model="form.name",
                placeholder="Alan Turing",
                name="full-name".
                required
            )
        b-form-group(
            id="contact-group-3",
            label="Your Message:",
            label-for="contact-input-3",
            description="Read by robots, virtual assistants, and possibly Johnathan himself."
        )
            b-form-textarea(
                id="contact-input-3",
                v-model="form.content",
                placeholder="Johnathan, I'd like to get in touch with you about...",
                rows="6",
                name="message",
                max-rows="10"
            )
        b-button(
            type="submit",
            variant="secondary",
            size="lg"
        ) Submit
</template>

<script>
export default {
  name: 'FormContact',
  data() {
    return {
      form: {
        email: '',
        name: '',
        content: '',
      },
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert('Not currently implemented.');
    },
  },
};
</script>

<style scoped>
    #contact-form {
        padding: 0.5em;
        margin: 0.5em;
    }
</style>
