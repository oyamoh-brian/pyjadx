#include <iostream>
#include <jadx/jadx.hpp>
#include "core.hpp"

int main(void) {
  std::unique_ptr<jni::Jadx> jadx{new jni::Jadx{}};
  jadx->load("/tmp/com.passwordchecker.apk");
  return 0;
}
