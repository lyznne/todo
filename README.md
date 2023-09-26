 <div class="bio-box">
                            {% if userDetail.bio %}

                            <div class="with-bio">
                                <div class="show-bio">
                                    <p>{{ userDetail.bio }}</p>
                                    <span>Bio</span>
                                </div>
                            </div>
                            {% else %}
                            <div class="without-bio">
                                <div class="bio-input-field">
                                    <label for="bio">Add bio</label>
                                    <textarea name="bio" id="bio" cols="10" rows="5"
                                        placeholder="Tell us something about yourself"
                                        value="{{ userDetail.bio }}"></textarea>
                                </div>
                            </div>
                            {% endif %}
                        </div>
