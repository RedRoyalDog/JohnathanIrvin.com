<template lang='pug'>
  p.
    {{written}}#[span(:class="{ hidden: !isVisible }") _]#[span(:class="{ hidden: isVisible }") {{'\u00A0'}}]
</template>

<script>
export default {
    props: [
        'text'
    ],
    data: function() {
        return {
            isVisible: false,
            written: '',
            // During a light test I typed 485 chars in 1 min.
            // This is around 8 characters per second --- around 95 WPM.
            // My maximum typing speed is 140 WPM, but we'll use this
            // as my typing speed is already fast as is.
            //
            // After initial testing, apparently I type way too faster --- divide by 2 for around  47.5 wpm.
            typingSpeed: 1000 / (485 / 60), // Typing speed in characters per millisecond. 

            blinkSpeed: 1000, // Blink speed in milliseconds.
        }
    },
    methods: {
        ran: function(low, high) {
             return Math.random() * low + high;
        },
        incrementWord: function() {
            if (this.text === this.written) {
                return;
            } else {
                window.setTimeout(this.incrementWord, this.typingSpeed + this.ran(10, 20)); 
            }
            let lenWritten = this.written.length;
            this.written += this.text[lenWritten];
        },
        blink: function() {
            this.isVisible = !this.isVisible;
            window.setTimeout(this.blink, this.blinkSpeed); 
        }
    },
    created: function() {
        this.written += this.text[0];
        window.setTimeout(this.incrementWord, this.typingSpeed + this.ran(10, 20)); 
        window.setTimeout(this.blink, this.blinkSpeed); 
    }
}
</script>

<style>
.hidden {
    display: none;
}
</style>