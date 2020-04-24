class SwaggerParser(object):
    def gen_api(self, filt_type=json):
        #create dictionary
        _make_dirctionary_for_tags(tags_list)
        apis_list = _make_apis(paths_dict)  #api have exists correct dir
        for api in apis_list:
            #api = {'tag_name', 'api_dict'}
            if file_type = json:
                utils.dump_json(api.api_dict, "api/pet/xxx.json")
            else
                utils.dump_yaml(api.api_dict, new_file_path)

    def _make_dictionary_for_tags(self, tags_list):
        for tag in tags_list:
            #create folder for tag.name


    def _make_apis(self, paths_dict):
        apis_list = []
        for key, value in paths_dict:
            # judge exclude/filter
            (tag_name ,api_dict) = _make_api(key, value)
            apis_list.append((tag_name ,api_dict))
        return apis_list

    def _make_api(self, key, value):
        api_dict = {
            "name":"",
            "variables": {},
            "request":{},
            "base_url":f"http://xxxxx/{key}",
            "validate":[]
        }
        _prepare_name(api_dict, value)
        _prepare_variables(api_dict, value)
        _prepare_request(api_dict, value)
        _prepare_validate(api_dict, value)
        return api_dict

    def _prepare_name(self,api_dict ,value):
        pass

    def _prepare_request(self,api_dict, value):
        _make_request_url(api_dict, value)
        _make_request_method(api_dict, value)
        _make_request_headers(api_dict, value)
        _make_request_data(api_dict, value)

    def _prepare_validate(self,api_dict, value):
        pass






