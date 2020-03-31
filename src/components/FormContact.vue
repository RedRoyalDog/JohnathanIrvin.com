/*
 * Created on Tue Mar 31 2020 by Johnathan Irvin
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

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
