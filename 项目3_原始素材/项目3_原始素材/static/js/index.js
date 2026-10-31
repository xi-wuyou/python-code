const app = new Vue({
    el: '#app',
    data() {
        return {
            nums: [
                0,
                0,
                0,
                0,
                0
            ],
            value: null,
            result: []
        }
    },
    methods: {
        handleClick() {
            if (this.value === null) {
                return this.$message.error("请先选择计算方式")
            }
            $.ajax({
                url: '/data',
                method: 'post',
                data: JSON.stringify({
                    nums: this.nums,
                    type: this.value
                }),
                contentType: 'application/json',
                success: function (result) {
                    app.result.push(result.result)
                }
            })
        }
    }
})