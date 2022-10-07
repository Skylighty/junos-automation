#!/bin/bash

#COLOR CODES
RED='\033[0;31m'
GREEN='\033[0;32m'
YELL='\033[0;33m'
NC='\033[0m'
#END OF COLOR CODES

echo -e "${YELL}Updating & upgrading OS${NC}." && \
sudo apt-get update -y && \
sudo apt-get upgrade -y && \
echo -e "${GREEN}OK.${NC}" && \
echo -e "Installing ${YELL}libffi-dev${NC}." && \
sudo apt-get install -y libffi-dev && \
echo -e "${GREEN}OK.${NC}" && \
echo -e "Installing ${YELL}libssl-dev${NC}." && \
sudo apt-get install -y libsll-dev && \
echo -e "${GREEN}OK.${NC}" && \
echo -e "Installing ${YELL}libxml2-dev${NC}." && \
sudo apt-get install -y libxml2-dev && \
echo -e "${GREEN}OK.${NC}" && \
echo -e "Installing ${YELL}libxslt1-dev${NC}." && \
sudo apt-get install -y libxslt1-dev && \
echo -e "${GREEN}OK.${NC}" && \
echo -e "Installing ${YELL}python3-dev${NC}." && \
sudo apt-get install -y python3-dev && \
echo -e "${GREEN}OK.${NC}"

echo -e "${GEREN}OK${NC}. OS-level requirements installed."
echo -e "Installing ${YELL}Junos PyEZ${NC} using ${RED}pip${NC}"
sudo pip3 install junos-eznc && \
echo -e "${GREEN}OK.${NC}"