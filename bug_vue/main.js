const CustomButton = {
    props: {
        label: String
    },
    template: `<button @click="clickButton">{{ label; }}</button>`,
    methods: {
        clickButton() {
            alert("カスタムボタンがクリックされました！");
        }
    }
};

new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        inputMessage: ''
    },
    methods: {
        updateMessage() {
            message = inputMessage;
        }
    }
});
