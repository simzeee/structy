// My wack solution
const isPrime1 = (n) => {
  if (n === 1) return false;
  let divisible = 0;
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      divisible += 1;
    }
  }
  if (divisible > 2) {
    return false;
  } else return true;
};

// Alvin's Solution

const isPrime2 = (n) => {
  if (n < 2) return false;

  for (let i = 2; i <= Math.sqrt(n); i += 1) {
    if (n % i === 0) return false;
  }

  return true;
};

// n = input number
// Time: O(square_root(n))
// Space: O(1)
