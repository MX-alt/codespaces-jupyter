function isFlipedString(s1: string, s2: string): boolean {
    if (typeof s1 !== "string" || typeof s2 !== "string") {
        throw new TypeError("Inputs must be strings.");
    }

    if (s1.length !== s2.length) {
        return false;
    }

    if (s1.length === 0) {
        return true;
    }

    return s2.includes(s1 + s1);
}

console.log(isFlipedString("waterbottle", "erbottlewat"));
console.log(isFlipedString("abcde", "cdeab"));
console.log(isFlipedString("abcde", "abced"));
