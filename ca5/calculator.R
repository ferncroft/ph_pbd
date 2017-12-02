### caclulator function selection
get_algor <- function() {
  s <- readline("Select (A)dd,(S)ubtract,(M)ultiply,(D)ivide,(E)xponential,S(Q)uare Root,(F)actorial,(L)og,(P)erimeter of circle,Si(N),E(X)it")
  s = toupper(s)
  if (s %in% c('A','S','M','D','E','Q','F','L','P','N','X')) {
    return (s)
  }
}

### ensure entry is a numeric
readnumeric <- function(whichno) { 
  if (whichno = '1st') {
    n <- readline("Enter 1st number: ")
  } 
  else {
    n <- readline("Enter 2nd number: ")
  }
  n <- as.numeric(n)
  if (is.na(n)){
    n <- readnumeric(whichno)
  }
  return(n)
}

### define mathematical functions
calc_add <- function(x,y) {
  return <- x+y
}

calc_subtract <- function(x,y) {
  return <- x-y
}

calc_multiply <- function(x,y) {
  return <- x*y
}

calc_divide <- function(x,y) {
  return <- x/y
}

calc_exponent <- function(x,y) {
  return <- x^y
}

calc_factorial <- function(x) {
  return <- factorial(x)
}

calc_log <- function(x) {
  return <- log2(x)
}

calc_sin <- function(x) {
  return <- sin(x)
}

calc_circleperimeter <- function(x) {
  return <- 2 * pi * x
}

getfunc = ''

while (getfunc != 'X') {
  # get the mathematical function to apply
  getfunc = get_algor()
  if (getfunc=='X') {
    exit()
  }
  # get the first numeric
  a = readnumeric('1st')

  # get a second numeric if required
  if (getfunc %in% c('A','S','M','D','E')) {
    b = readnumeric('2nd')
  }

  # apply and print the calulation
  if (getfunc == 'A') {
    print(calc_add(a,b))
  } else if (getfunc == 'S') {
    print(calc_subtract(a,b))
  } else if (getfunc == 'M') {
    print(calc_multiply(a,b))
  } else if (getfunc == 'D') {
    print(calc_divide(a,b))
  } else if (getfunc == 'E') {
    print(calc_exponent(a,b))
  } else if (getfunc == 'Q') {
    print(calc_exponent(a,0.5))
  } else if (getfunc == 'F') {
    print(calc_factorial(a))
  } else if (getfunc == 'L') {
    print(calc_log(a))
  } else if (getfunc == 'N') {
    print(calc_sin(a))
  } else if (getfunc == 'P') {
    print(calc_circleperimeter(a))
  } else print("invalid entry")

}

