<template lang='pug'>
  p.
    {{written}}#[span(:class="{ hidden: !isVisible }") _]#[span(:class="{ hidden: isVisible }") {{'\u00A0'}}]
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            default: ''
        },
        hideCursor: {
            type: Boolean,
            default: false
        },
        typingSpeed: {
            type: Number,
            // During a light test I typed 485 chars in 1 min.
            // This is around 8 characters per second --- around 95 WPM.
            // My maximum typing speed is 140 WPM, but we'll use this
            // as my typing speed is already fast as is.
            // 1 Second / Character Per Minute == 1 key per X milliseconds.
            default: 1000 / (485 / 60), // Typing speed in characters per millisecond. 
        },
        blinkSpeed: {
            type: Number,
            default: 1000 // Cursor Blink speed in milliseconds.
        }, 
    },
    data: function() {
        return {
            isVisible: false,
            written: '',
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
                setTimeout(this.incrementWord, this.typingSpeed + this.ran(10, 20)); 
            }
            let lenWritten = this.written.length;
            this.written += this.text[lenWritten];
        },
        blink: function() {
            this.isVisible = !this.isVisible && !this.hideCursor;
            setTimeout(this.blink, this.blinkSpeed); 
        }
    },
    created: function() {
        this.written += this.text[0];
        setTimeout(this.incrementWord, this.typingSpeed + this.ran(10, 20)); 
        setTimeout(this.blink, this.blinkSpeed); 
    }
}
</script>

<style>
.hidden {
    display: none;
}
</style>