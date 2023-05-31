include_directories("../")
AUX_SOURCE_DIRECTORY(${PROJECT_SOURCE_DIR}/rtksrc/rcv rcv_src)
add_library(rcv SHARED ${rcv_src})
