def gcd(x, y):  # x > y
  x0, x1, y0, y1 = 1, 0, 0, 1
  while (y > 0):
    print('\\gcd(%d, %def) &: %d &&= ' % (x, y, x), end='')
    q, r = divmod(x, y)
    # print('%d \\times %d + %d &&\\quad' % (q, y, r), end='')
    # print('[%d, %d] - %d[%d, %d] = ' % (x0, x1, q, y0, y1), end='')
    x, y = y, r
    x0, x1, y0, y1 = y0, y1, x0 - q * y0, x1 - q * y1
    # print('[%d, %d] \\\\' % (y0, y1))
  return x, x0, x1
