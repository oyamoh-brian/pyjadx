target_sources(jadxjni
  INTERFACE
  "${CMAKE_CURRENT_LIST_DIR}/Logger.hpp"
  "${CMAKE_CURRENT_LIST_DIR}/Logger.cpp"

  "${CMAKE_CURRENT_LIST_DIR}/LoggerFactory.hpp"
  "${CMAKE_CURRENT_LIST_DIR}/LoggerFactory.cpp"
)
