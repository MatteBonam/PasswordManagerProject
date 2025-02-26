class ImportParser:
    @staticmethod
    def parse_line(line, format_string):
        result = {
            'service': 'IMPORTATO',
            'username': 'IMPORTATO',
            'password': 'IMPORTATO'
        }
        
        format_parts = ImportParser.tokenize_format(format_string)
        current_text = line
        
        for part in format_parts:
            if part.startswith('$'):
                var_name = part[1:]
                if current_text:
                    value, current_text = ImportParser.extract_next_value(current_text, format_parts)
                    if var_name in ['service', 'username', 'password']:
                        result[var_name] = value.strip('"').strip("'")
            else:
                if current_text.startswith(part):
                    current_text = current_text[len(part):].lstrip()
        
        return result

    @staticmethod
    def tokenize_format(format_string):
        tokens = []
        current_token = ''
        i = 0
        
        while i < len(format_string):
            if format_string[i] == '$':
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                var = '$'
                i += 1
                while i < len(format_string) and format_string[i].isalpha():
                    var += format_string[i]
                    i += 1
                tokens.append(var)
                continue
            current_token += format_string[i]
            i += 1
        
        if current_token:
            tokens.append(current_token)
        
        return tokens

    @staticmethod
    def extract_next_value(text, format_parts):
        text = text.lstrip()
        next_separator = None
        for part in format_parts:
            if not part.startswith('$') and part in text:
                pos = text.find(part)
                if next_separator is None or (pos < text.find(next_separator) and pos != -1):
                    next_separator = part
        
        if next_separator:
            parts = text.split(next_separator, 1)
            return parts[0].strip(), (next_separator + parts[1] if len(parts) > 1 else '')
        return text.strip(), ''