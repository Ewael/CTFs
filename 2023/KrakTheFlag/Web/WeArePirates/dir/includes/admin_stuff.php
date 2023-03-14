<?php

class CheckStatus
    {
        public $status;
        function __toString()
        {
            $handle = popen($this->status,"r");
            return fread($handle, 2096);
        }
    }

?>

