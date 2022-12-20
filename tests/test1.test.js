pm.test("ТЕСТ", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 202]);
});